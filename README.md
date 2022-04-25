# Shadow's Python Discord Bot Template
## _Making Bot Development SIMPLE_

You do not need to know how to code in order to use this template.
It's basically a "fill in the gaps" kinda thing. Everything has been labelled for you.
Though, *some* programmer knowledge is necessary, as well as an ambition to learn.

**BEFORE DOWNLOADING:**
- Please note that if you decide to just "Download as .ZIP" instead of using a git clone client/command, you will have an issue with the cog file pathing.
The folder structure needs to be like this: Bot Folder > Code

Having another folder inside will break it. I know I suck at explaining, so here's some pics:

![1](https://is-dumb.today/bCye5xVMF.png)
![2](https://is-dumb.today/LBj0wNPSWo.png)

## How to Use:

- Download Python from here: [https://www.python.org/]
- After Python is correctly installed, open your terminal/cmd of choice and type `py -3 -m pip install -U nextcord`.
- You'll also need to type `pip install -U jishaku` to install Jishaku (which this bot uses for debugging).
- You'll also need to type `pip install aiohttp` to install aiohttp which this bot uses.
- You'll also need to type `python -m pip install requests` for error handling.
- Clone this repo and fill in the blanks. You will get errors if you do not replace every marked command.
- After everything is edited to your liking, you can run `bot.py`. For Linux, the command is `python3 bot.py`.

## Features

This bot features "cogs", which are separate .py files that contain commands.

| Cog Name | Description |
| ------ | ------ |
| `Application.py` | This cog supports Application Commands such as slash commands, app menu for user and messages! |
| `Debug.py` | These are the basic debug commands like `[p]ping` and `[p]botinfo`. |
| `Fun.py` | Basic fun commands like `[p]roll` and `[p]8ball`. |
| `Help.py` | Advanced Help Menu with pagination! Have different pages for different categories of commands. |
| `Moderation.py` | Basic moderation commands like `[p]ban`. |
| `Owner.py` | Bot Developer commands to see stats about the Servers the bot is in, as well as the ability to remove the bot from any server. |
| `Reload.py` | Easily reload cogs whenever you make a live change. `[p]reload [cogname]`. |
| `Sendembed.py` | Send embed messages with ease! |

## License

This bot can be used to make any Discord Bot of your choice. It is completely open-source for Non-Commercial purposes. Do not attempt to resell this code. You do not need to leave credits to me for developing the code, but please do not sell it as your own.

## Credits

- Developer & Repository Manager: **Shadowstar#7815**
- 8ball Command: **Ellie#0080**
- Example in code: **Fran[She/They]#0666**
- Special Thanks: **DuckMasterAl#0001**
