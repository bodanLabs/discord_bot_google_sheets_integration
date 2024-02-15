# Discord Bot for Google Sheets Integration

This Discord bot integrates with Google Sheets to provide commands within Discord for displaying a leaderboard and individual ranks based on data stored in a Google Sheet. It utilizes the Discord.py library along with Google Sheets API for real-time data interaction.

## Features
- Leaderboard Display: Show a top 10 leaderboard directly in a Discord channel.
- Individual Rank Display: Provide users with their current rank and statistics.
- Dynamic Color Embeds: Embed messages in Discord have dynamically changing colors for visual variety.


## Requirements
- Python 3.6+
- discord.py
- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client
- pandas

## Setup Instructions
### Clone the Repository:
```git clone <repository-url>```
```cd <repository-directory>```
### Install Dependencies:
```pip install -r requirements.txt```
### Configure Google Sheets API:
- Follow Google's guide to create a service account and enable the Google Sheets API.
https://developers.google.com/sheets/api/quickstart/python
- Download the credentials file (creds.json) and place it in the bot's directory.
### Configure the Bot:
- Create a config.json file in the bot's directory with the following structure:
`{
  "token": "YOUR_DISCORD_BOT_TOKEN",
  "guildID": "YOUR_GUILD_ID",
  "sheetID": "YOUR_GOOGLE_SHEET_ID"
}
` 
- Replace "YOUR_DISCORD_BOT_TOKEN", "YOUR_GUILD_ID", and "YOUR_GOOGLE_SHEET_ID" with your Discord bot token, Discord guild (server) ID, and Google Sheet ID, respectively.
### Run the Bot:
```python bot.py```

## Usage
After setting up the bot and inviting it to your Discord server, you can use the following commands:

- /setup: Initializes the connection to Google Sheets and prepares the leaderboard.
- /rank <username>: Displays the rank and statistics of the specified username from the Google Sheets data.

## Contributions
Contributions are welcome! Please create a pull request or issue for any bugs, features, or enhancements.
