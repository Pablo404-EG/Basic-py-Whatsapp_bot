import os
from pywhatsapp import WhatsAppClient
from utils.logger import setup_logger

client = WhatsAppClient(session_file="session.json")
logger = setup_logger()

def load_commands():
    commands_dir = './commands'
    for file in os.listdir(commands_dir):
        if file.endswith('.py'):
            __import__(f'commands.{file[:-3]}')
            logger.info(f'Command {file} loaded.')

def main():
    try:
        client.connect()
        logger.info("Bot connected successfully.")
        load_commands()
        client.listen()
    except Exception as e:
        logger.error(f'Error occurred: {e}')

if __name__ == "__main__":
    main()
  
