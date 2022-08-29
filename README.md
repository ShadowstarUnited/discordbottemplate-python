# Shadow's Python Discord Bot Template
## _Making Bot Development SIMPLE_

You do not need to know how to code in order to use this template.
It's basically a "fill in the gaps" kinda thing. Everything has been labelled for you.
Though, *some* programmer knowledge is necessary, as well as an ambition to learn.

**BEFORE DOWNLOADING:**
- Most of this code comes from snippets of my own bot [Drunk o'Bot](https://www.drunkobot.com/) and thus is not thoroughly tested in this form.
That being said, if there are errors or issues, you can join Team Hydra to contact me. You may ping me in the #other-support: [https://discord.gg/zira]
- This bot uses the Nextcord library. If you need help with nextcord or python, I would highly recommend you join [https://discord.gg/nextcord] and use the #help form.
- Please note that if you decide to just "Download as .ZIP" instead of using a git clone client/command, you will have an issue with the cog file pathing.
The folder structure needs to be like this: Bot Folder > Code

Having another folder inside will break it. I know I suck at explaining, so here's some pics:

![1](https://is-dumb.today/bCye5xVMF.png)
![2](https://is-dumb.today/LBj0wNPSWo.png)

## How to Use:

- Download Python from here: [https://www.python.org/]
- After Python is correctly installed, clone this repo or download as zip.
- Open your terminal/cmd of choice and type `python3 -m pip install -r requirements.txt` (You may need to specify a path, in which case: `pip install -r /path/to/requirements.txt`) and then fill in the blanks in all the cogs. You will get errors if you do not replace every marked command.
- You will need to set up your own MongoDB (It's free). This template does not and will not show you how to do so. [https://www.mongodb.com/]
- After everything is edited to your liking, you can run `bot.py`. For Linux, the command is `python3 bot.py`.

## Features

This bot features "cogs", which are separate .py files that contain commands.
This bot uses MongoDB as a Database, using motor. This is required for the bot to function.

| Cog Name | Description |
| ------ | ------ |
| `Application.py` | This cog supports Application Commands such as slash commands, app menu for user and messages! |
| `Blacklist.py` | This cog allows you to blacklist users/guilds from using your bot. You can also whitelist them. |
| `Configs.py` | This cog allows for custom bot prefixes per server. |
| `Debug.py` | These are the basic debug commands like `[p]ping` and `[p]botinfo`. |
| `Fun.py` | Basic fun commands like `[p]roll` and `[p]8ball`. |
| `Help.py` | Advanced Help Menu with pagination! Have different pages for different categories of commands. |
| `Logs.py` | This cog logs when your bot joins/leaves a server. |
| `Moderation.py` | Basic moderation commands like `[p]ban`. |
| `Owner.py` | Bot Developer commands to see stats about the Servers the bot is in, as well as the ability to remove the bot from any server. |
| `Reload.py` | Easily reload cogs whenever you make a live change. `[p]reload [cogname]`. |
| `Sendembed.py` | Send embed messages with ease! |

## License

This bot can be used to make any Discord Bot of your choice. It is completely open-source for Non-Commercial purposes. Do not attempt to resell this code. You do not need to leave credits to me for developing the code, but please do not sell it as your own.

## Credits

- Developer & Repository Manager: **Shadowstar#7815**
- Configs, guild logging, blacklisting, botinfo & sendembed developer: **RPrime#2003** - Special thanks
- 8ball Command: **Ellie#0080**
- Example in code: **Fran[She/They]#0666**
