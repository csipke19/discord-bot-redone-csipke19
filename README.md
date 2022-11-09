# All around Discord bot🤖

This is a bot made for our personal needs on our discord server, but if you are interested, you can use this as a bot logic for your own<br>
Unfortunately **we can't provide you our own bot, but here is a short guide how you can make your own bot for this purpose!**<br>
If you want to test the bot out, here is an invitation link to the test server: [link](https://discord.gg/x3edBH3cSJ)

## Setup your own bot steps🔧
1. [Create a bot](#create-a-bot)
2. [Invite your bot to your server](#invite-your-bot-to-your-server)
3. [Integrate your bot](#integrate-your-bot)<br>
[FAQ](#faq)

## Create a bot
First, [click here](https://discord.com/developers/docs/intro) to get to the **Discord Developer Portal**<br>
In here, you need to click the applications button on the left hand corner<br>
![image](https://user-images.githubusercontent.com/90270578/200140829-605d5abc-420f-47d3-aa51-8d2466321366.png)<br><br>
If you are on the application page, you need to create a new application, to do this, click the button on the right hand corner<br>
![image](https://user-images.githubusercontent.com/90270578/200140886-cd0e4815-4d49-48b9-82a4-b6dd9661a10e.png)<br><br>
Add a name to it and get inside your application<br>
When you are inside, you are going to see a settings menu on the left hand side, click the Bot menu button<br>
![image](https://user-images.githubusercontent.com/90270578/200141052-2c8b3b5d-c029-4317-800b-21797e9721c5.png)<br><br>
Here, create your own bot, give it a name and make the following settings (not every one of them is necessary, but some of them is nice to have)<br>
<img src="https://user-images.githubusercontent.com/90270578/200141203-54a38686-b6be-4006-b14c-4682dd2c9279.png" width="700"><br><br>
If you are DONE, copy the discord **Bot token code** on this page (later you need this), your token code is the long letter-number combination near the top. If you not see it by default, Click the `Reset Token` Button<br>
![image](https://user-images.githubusercontent.com/90270578/200141703-c4dff982-4b0d-4fe8-9601-df0e607c865d.png)<br><br>

## Invite your bot to your server
In the next step, you need to get your client id, and paste it in the following link:<br>

>discord.com/api/oauth2/authorize?client_id=`|Your client ID|`&permissions=0&scope=bot%20applications.commands<br>

To get your client ID, you need to click the OAuth2 button on the left menu and look for the client ID on the middle, like the following:<br>
![image](https://user-images.githubusercontent.com/90270578/200170927-92e04c72-ce50-4928-a126-77712599b3e9.png)<br><br>
Paste your client code to the previous URL and copy it to a new browser page. After a while, you get a similar look<br>
Here, choose the server you want the bot to connect to and click the `Authorize` button on the bottom
![image](https://user-images.githubusercontent.com/90270578/200170522-eca16f9a-19ca-4cdc-b8ff-8d3d5ecedac7.png)<br><br>
If everything was right, you get the following comfirmation page:<br>
![image](https://user-images.githubusercontent.com/90270578/200170503-a01c19b5-c92c-45c8-9b85-a0e53547dcdf.png)<br><br>

## Integrate your bot 
If you cloned this git repository, you need to create a csv file to use your bot with the **previously cloned token**<br><br>
>The error messeage if the file is missing<br>
![image](https://user-images.githubusercontent.com/90270578/200693022-4d4edd06-f1b2-462d-b852-9900c820b136.png)<br><br>

To resolve this problem, you need to do a directory with the name: "csv_files" in the main folder like the following:<br>
![image](https://user-images.githubusercontent.com/90270578/200694389-6c80f61c-fc46-4618-a226-5ea0a9c338fb.png)<br><br>
..and in this directory, do a file, with the name: "code.csv"<br>
![image](https://user-images.githubusercontent.com/90270578/200695080-1e589745-4d70-4fb3-8319-31b0c3c28baa.png)<br>
Just paste your token in this file, save it and you are done!<br><br>
After this, you need to write in the Server ID to the "settings.cfg"<br>
To get your server ID, right click on your server on Discord, and press the `Copy ID` button on the bottom<br>
![image](https://user-images.githubusercontent.com/90270578/200828753-c1e6fdef-a2fd-4aaa-ae76-5ab4ccf0e189.png)<br><br>
..and copy it in to the settings.cfg, after the "server_id=" row like the following:<br>
![image](https://user-images.githubusercontent.com/90270578/200829323-8ab1c62a-e8d3-4e33-b3a9-a81b19fb1ca8.png)<br><br>

After this, if you run the "run.bat" file in the main folder you get the following look!<br>
![image](https://user-images.githubusercontent.com/90270578/200695432-70cc4033-dbc3-4689-9389-c279889798e3.png)<br><br>

## FAQ

### I got an error with "discord" module, what is this?
If you get this error, it means your requirement to run this bot is not met. To fix this, you need to install them with the file "requirements.txt".<br>
`disclaimer: the virtual enviroment creation (first 3 step) is only optional, but it's much easier to work with it later`
```
LINUX:
| pip install virtualenv | (if you don't already have virtualenv installed)
| virtualenv venv | to create your new environment (called 'venv' here)
| source venv/bin/activate | to enter the virtual environment
| pip install -r requirements.txt | to install the requirements in the current environment

WINDOWS:
| pip install virtualenv | (if you don't already have virtualenv installed)
| python -m venv venv | to create your new environment (called 'venv' here)
| venv\Scripts\activate | to enter the virtual environment
| pip install -r requirements.txt | to install the requirements in the current environment
```

### I got this error: AttributeError: 'NoneType' object has no attribute 'voice_channels'. Why?
You get this error if you forgot to put in your server id in the "settings.cfg" file or the code you use is invalid, because the bot is not on the server or you missed out 1 or more number from the id. Step by step [in the following point](#integrate-your-bot)
