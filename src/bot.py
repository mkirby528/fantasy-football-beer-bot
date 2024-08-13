# bot.py
from os import getenv
import discord
from dotenv import load_dotenv
from src.espn import get_zero_point_teams
from src.discord_ids import get_discord_name
from src.nfl_weeks import get_current_week


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

        print("About to send")
        week = get_current_week()
        teams = get_zero_point_teams(week)
        output_string = f"Week {week} team owners with players who scored zero or below points:"
        for team in teams:
            owner_name = team.owners[0].get("firstName") + " " + team.owners[0].get("lastName")
            print(owner_name)
            output_string += "\n\t"
            players_string = ",".join(teams[team])
            output_string += f"{team.team_name} ({get_discord_name(owner_name)}): {players_string}"
        output_string += "\n"
        output_string += "Per the league charter you have one week to post video evidence of you shotgunning a beer otherwise you will recieve a 10 point penalty for next week's matchup."
        print(output_string)
        await channel.send(output_string)

        print("Sent")
        await client.close()
        return 1
    client.run(TOKEN)
