# hash-answer-discord-bot

 A simple discord bot that responds to messages from any user, the response contains SHA256 encryption on the message content + author name + author id + message date.

## Install dependencies
```
pip3 install -U discord.py
pip3 install -U python-dotenv
```
## Setup .env file
```
DISCORD_TOKEN={your_discord_token}
```
## Run
```
python3 main.py
```