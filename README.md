# pluuhh

## Description

This is a fun little project to get to know how Discord bots work. It is a simple bot that will send a link if it detects a certain keyword in a message. The keywords and their respective links can be found in `src/keywords.yaml`. Currently, it's just the Git tutorial link because that was the inspiration for this bot. A few friends always made fun of me for sending the link when people would ask for help with Git, so I thought it would be fun to automate it.

## Notes

1. you must have a `.env` file with the `DISCORD_TOKEN` variable set to your bot's token
2. This bot will only work if the message is sent in a channel whose name matches the following RegEx: `plu+h+`. 

## Invite the bot to your server

https://discord.com/oauth2/authorize?client_id=1330663644001734676&permissions=11264&integration_type=0&scope=bot