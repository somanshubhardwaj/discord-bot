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



