import asyncio
import random

from discord import ui, app_commands
from discord.ui import Button,View
import discord
import logging
from discord.ext import tasks
import json
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2 import service_account



logging.basicConfig(level=logging.INFO)



f = open('config.json')
datac = json.load(f)
guildID = datac['guildID']
token = datac['token']
sheetID = datac['sheetID']

TOKEN = token

intents = discord.Intents.all()
colors = [1752220,1146986,3066993,2067276,3447003,2123412,10181046,7419530,15277667,11342935,15844367,12745742,15105570,11027200,15158332,10038562,9807270,9936031,8359053,12370112,3426654,2899536,16776960]
color = random.choice(colors)

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=guildID))
            self.synced = True
            print(f"We have logged in as {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)



@tree.command(guild=discord.Object(id=guildID),name = "setup",description="setup")
async def setup(interaction: discord.Interaction):

    SERVICE_ACCOUNT_FILE = 'creds.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    credentialss = None
    credentialss = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    spreadsheetID =sheetID
    service = build('sheets', 'v4', credentials=credentialss)
    sheet = service.spreadsheets()
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetID, range='Raw Data!A1:D1000').execute()
    values = result.get('values', [])
    embed = discord.Embed(title="🏆 Leaderboard 🏆",
                          description="**Top 10**")
    x = 1
    for value in values[1:11]:
        if x == 1:
            xx = f"{x}🥇"
        elif x == 2:
            xx = f"{x}🥈"
        elif x == 3:
            xx = f"{x}🥉"
        else:
            xx = f"{x}🏅"
        embed.add_field(name=f"#{xx} {value[1]}",value=f"*Total L17* `{value[2]}` | *Total WC* `{value[3]}`",inline=False)
        x += 1
    await interaction.response.defer()
    await asyncio.sleep(0)
    msg = await interaction.followup.send(embed=embed)
    while True:
        color = random.choice(colors)
        result = service.spreadsheets().values().get(spreadsheetId=spreadsheetID, range='Raw Data!A1:D1000').execute()
        values = result.get('values', [])
        embed = discord.Embed(title="🏆 Leaderboard 🏆",
                              description="**Top 10**",color=color)
        x = 1
        for value in values[1:11]:
            if x == 1:
                xx = f"{x}🥇"
            elif x == 2:
                xx = f"{x}🥈"
            elif x == 3:
                xx = f"{x}🥉"
            else:
                xx = f"{x}🏅"
            embed.add_field(name=f"#{xx} {value[1]}", value=f"*Total L17* `{value[2]}` | *Total WC* `{value[3]}`",
                            inline=False)
            x += 1
        await msg.edit(embed=embed)
        await asyncio.sleep(60)




@tree.command(guild=discord.Object(id=guildID),name = "rank",description="rank")
async def rank(interaction: discord.Interaction,username:str):
    SERVICE_ACCOUNT_FILE = 'creds.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    credentialss = None
    credentialss = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    spreadsheetID = sheetID
    service = build('sheets', 'v4', credentials=credentialss)
    sheet = service.spreadsheets()
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetID, range='Raw Data!A1:D1000').execute()
    values = result.get('values', [])
    for value in values:
        if value[1] == username:
            rank = value[0]
            totalL17 = value[2]
            totalWC = value[3]
            embed = discord.Embed(title = f"#{rank} - {username}",
                                  description=f"📋 *Username*: `{username}`\n"
                                              f"🎖️ *Current rank*: `#{rank}`\n"
                                              f"⚜️*Total L17*: `{totalL17}`\n"
                                              f"⚜️*Total WC*: `{totalWC}`\n",color=color)
            await interaction.response.defer()
            await asyncio.sleep(0)
            await interaction.followup.send(embed=embed)




aclient.run(token)