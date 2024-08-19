from pywhatsapp import WhatsAppClient
from utils.logger import logger

def hello_command(client: WhatsAppClient, message):
    if message.text == "مرحبا":
        client.send_message(message.chat_id, "مرحبا بك كيف يمكنني مساعدتك اليوم")
        logger.info(f'Replied to {message.chat_id} with greeting.')

client.add_command("hello", hello_command)
