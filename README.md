# WelcomeBot

WelcomeBot is a simple Discord bot designed to welcome new members to your server. 
It sends a personalized greeting message in a designated `#welcome-channel` and provides a link to an onboarding document to help new members get started.

## Features
- Automatically detects new members joining the server.
- Sends a welcome message in a specified channel, greeting the new member by username.

## Requirements
- Python 3.8+
- All required dependencies are listed in `requirements.txt`.

## Installation
git clone https://github.com/albina777/WelcomeBot.git
cd WelcomeBot

## Create and acticate the virtual environment 
`python3 -m venv bot_env`

`source bot_env/bin/activate`  # For MacOS/Linux
`bot_env\Scripts\activate`     # For Windows

## Install dependencies
`pip install -r requirements.txt`

## Configure
Create a `.env` file in the project directory, and add your bot token:
DISCORD_TOKEN=your_bot_token_here
Replace your_bot_token_here with the actual bot token you obtained from the Discord Developer Portal.

## Usage
1. Run the bot
   `python welcome_bot.py`
2. When a new member joins your server, WelcomeBot will automatically send a welcome message in the `#welcome-channel`.
   Make sure the bot has permission to read and send messages in that channel.


## License
This project is licensed under the MIT License.



