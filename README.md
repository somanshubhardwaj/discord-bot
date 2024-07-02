# Discord Bot

A simple Discord bot built with Python and the `discord.py` library. This bot includes basic commands like ping, greeting, and arithmetic operations.

## Features

- Responds to a ping with "Pong!"
- Greets users with a hello or goodbye message.
- Adds two numbers.
- Provides a list of available commands.

## Prerequisites

Before setting up the bot, ensure you have the following installed:

- Python 3.8+
- Discord account and server
- Discord bot token

## For Relpit

- Go to [Repl](https://replit.com/@somanshubh/discord-bot?v=1)
- add TOKEN = your discord token to secrets

## Installation

1. Clone the repository or download the code:

   ```bash
   git clone https://github.com/somanshubhardwaj/discord-bot.git
   cd discord-bot
    ```


2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your bot token:

   ```env
   TOKEN=your-discord-bot-token
   ```

5. Run the bot:

   ```bash
   python main.py
   ```

## Usage

Once the bot is running, invite it to your server and use the following commands:

- `!ping`: Responds with "Pong!" to check if the bot is active.
- `!hello`: Sends a personalized greeting to the user.
- `!goodbye`: Sends a personalized goodbye message to the user.
- `!add <num1> <num2>`: Adds two numbers and returns the result.
- `!guide`: Lists the available commands and their usage.

## Code Overview

The bot is defined in `bot.py` and uses the `discord.ext.commands` extension to manage commands.

### Key Sections:

1. **Environment Variables**: Loaded using `python-dotenv` to securely manage sensitive information like the bot token.

   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()
   TOKEN = os.getenv('TOKEN')
   ```

2. **Bot Setup**: Defines command prefix, intents, and event handlers.

   ```python
   import discord
   from discord.ext import commands

   intents = discord.Intents.default()
   intents.message_content = True

   bot = commands.Bot(command_prefix='!', intents=intents)
   ```

3. **Commands**: Includes commands for ping, greetings, addition, and help guide.

   ```python
   @bot.command(name='ping')
   async def ping(ctx):
       await ctx.send('Pong!')

   @bot.command(name='hello')
   async def hello(ctx):
       await ctx.send(f'Hello {ctx.author.mention}!')

   @bot.command(name='goodbye')
   async def goodbye(ctx):
       await ctx.send(f'Goodbye {ctx.author.mention}!')

   @bot.command(name='add')
   async def add(ctx, num1: float, num2: float):
       result = num1 + num2
       await ctx.send(f'The sum of {num1} and {num2} is {result}')
   ```

4. **Error Handling**: Provides feedback for unknown commands and missing arguments.

   ```python
   @bot.event
   async def on_command_error(ctx, error):
       if isinstance(error, commands.CommandNotFound):
           await ctx.send("Sorry, I didn't recognize that command.")
       elif isinstance(error, commands.MissingRequiredArgument):
           await ctx.send("You're missing some required arguments for this command.")
       else:
           await ctx.send("An error occurred while processing the command.")
           raise error
   ```

5. **Running the Bot**: The bot is started using the token from environment variables.

   ```python
   bot.run(TOKEN)
   ```
## Using Docker

To set up and run your Discord bot using Docker, follow these instructions. This guide assumes you have Docker installed on your machine.

## Step-by-Step Instructions

### 1. Prerequisites

- Docker installed on your system.
- Discord bot token ready.
- The bot code, including the `bot.py` (or `main.py` as referenced in the Dockerfile) and a `requirements.txt` file with the necessary dependencies.

### 2. Project Structure

Ensure your project structure looks something like this:

```
/my-discord-bot
    ├── .env               # Environment variables file
    ├── main.py             # Your bot code
    ├── requirements.txt   # Python dependencies
    ├── Dockerfile         # Docker configuration
```



### 3. Creating the `.env` File

Create a `.env` file in the root of your project to securely store your bot token:

```env
# .env
TOKEN=your-discord-bot-token
```

Make sure this file is included in your `.gitignore` to prevent sensitive information from being shared.

### 4. Writing the `requirements.txt`

Your `requirements.txt` file should list all the dependencies your bot needs. For example:

```text
# requirements.txt
discord.py==2.0.0
python-dotenv==1.0.0
```

### 5. Building the Docker Image

Navigate to your project directory and build your Docker image using the following command:

```bash
docker build -t my-discord-bot .
```

- `-t my-discord-bot`: Tags the image with the name `my-discord-bot`.
- `.`: Specifies the current directory as the context for the Docker build.

### 6. Running the Docker Container

Run your bot in a Docker container with the following command:

```bash
docker run --env-file .env my-discord-bot
```

- `--env-file .env`: Loads environment variables from the `.env` file.
- `my-discord-bot`: Uses the image built in the previous step.

### 7. Managing and Stopping the Container

To list all running containers:

```bash
docker ps
```

To stop a running container, use its container ID from the list:

```bash
docker stop <container_id>
```

Replace `<container_id>` with the actual ID of your running container.



### Conclusion

You've successfully containerized your Discord bot and can now run it reliably in any environment that supports Docker. This approach simplifies the deployment process and ensures that your bot runs consistently across different environments.

Feel free to ask if you have any questions or need further assistance!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository and submit pull requests for any enhancements or bug fixes. Contributions are welcome!

## Acknowledgements

- [discord.py](https://github.com/Rapptz/discord.py) - Python library for Discord API.
- [python-dotenv](https://github.com/theskumar/python-dotenv) - To load environment variables from `.env` file.



