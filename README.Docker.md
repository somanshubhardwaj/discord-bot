# Using Docker

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


### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### References
* [Docker's Python guide](https://docs.docker.com/language/python/)