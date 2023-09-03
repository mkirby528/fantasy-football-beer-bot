# bot.py
import os

import discord
from dotenv import load_dotenv
from src.espn import get_zero_point_teams
from src.name_to_discord_map import get_discord_name

if os.getenv("DISCORD_GUILD") is None:
    load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = int(os.getenv('CHANNEL_ID'))

def send_message(event, context):
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        guild = discord.utils.get(client.guilds, name=GUILD)
        print(
            f'{client.user} is connected to the following guild:\n'f'{guild.name}(id: {guild.id})')

        channel = client.get_channel(CHANNEL)

        print("About to send")
        week = 1
        teams = get_zero_point_teams(week)
        output_string = f"Week {week} team owners with players who scored zero or below points:"
        for team in teams:
            output_string += "\n\t"
            players_string = ",".join(teams[team])
            output_string += f"{get_discord_name(team.owner)}: {players_string}"
        print(output_string)
        # await channel.send(output_string)

        print("Sent")
        await client.close()
        return 1
    client.run(TOKEN)
