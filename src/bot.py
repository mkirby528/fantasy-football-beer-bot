from os import getenv
import discord
from dotenv import load_dotenv
from src.espn import get_zero_point_teams
from src.discord_ids import get_discord_name
from src.nfl_weeks import get_current_week
from src.dynanmo import write_to_dynamo, update_with_fulfilled, get_unfulfilled_users_for_week
from datetime import datetime, timedelta

if getenv("DISCORD_GUILD") is None:
    load_dotenv()

TOKEN = getenv('DISCORD_TOKEN')
GUILD = getenv('DISCORD_GUILD')
CHANNEL = int(getenv('CHANNEL_ID'))


def send_message(event, context):
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        guild = discord.utils.get(client.guilds, name=GUILD)
        print(
            f'{client.user} is connected to the following guild:\n'f'{guild.name}(id: {guild.id})')

        channel = client.get_channel(CHANNEL)

        print("Discord Client initalized...")
        week_number = get_current_week()
        event_type = event.get("event_type")
        if event_type == "zero_check":
            output_string = get_past_week_zeroes_output(week_number)
            print("Output string: " + output_string)

            await channel.send(output_string)
            print("Sent message...")

        elif event_type == "video_check":
            await get_users_who_posted_videos(channel, week_number-1)
            unfulfilled_users = get_unfulfilled_users_for_week(week_number - 1)
            await channel.send(f"Users who have not posted a video for week {week_number - 1}: {str(unfulfilled_users)}. If believe this to be an error please message Matthew Kirby and he will fix it.")

        await client.close()
        return 1

    client.run(TOKEN)


def get_past_week_zeroes_output(week) -> str:
    teams = get_zero_point_teams(week)
    output_string = f"Week {week} team owners with players who scored zero or below points:"
    for team in teams:
        owner_name = team.owners[0].get("firstName") + " " + team.owners[0].get("lastName")
        discord_id = get_discord_name(owner_name)
        output_string += "\n\t"
        players_string = ",".join(teams[team])
        output_string += f"{team.team_name} ({discord_id}): {players_string}"
        write_to_dynamo({
            "week_number": week,
            "user_id": discord_id,
            "owner": owner_name,
            "players": teams[team],
            "fulfilled": False
        })
    output_string += "\n"
    output_string += (
        "Per the league charter you have one week to post video evidence of you "
        "shotgunning a beer otherwise you will receive a 10 point penalty for next week's matchup. "
        "When posting your video please tag the bot (@BeerBot) and post the week number "
        "(ie \"Week 1\" or \"week 1\") in the same post as your video so that the bot can know "
        "what week you are fulfilling."
    )
    return output_string


async def get_users_who_posted_videos(channel, week_number) -> list[str]:
    print(f"Searching for user mentions for week {week_number}...")

    messages = [msg async for msg in channel.history(limit=250, after=datetime.now() - timedelta(days=7)) if not msg.author.bot]
    for message in messages:
        for attachement in message.attachments:
            print("attachment", attachement)
            attachment_type, attachment_format = attachement.content_type.split(
                '/')
            if attachment_type == "video":
                update_with_fulfilled(week_number, f"<@{message.author.id}>")
                break
