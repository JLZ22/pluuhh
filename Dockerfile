FROM python:3.10-slim

WORKDIR /app
COPY src/bot.py /app/bot.py
COPY src/keywords.yaml /app/keywords.yaml
COPY .env /app/.env

RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install discord.py pyyaml python-dotenv

CMD ["python", "bot.py"]