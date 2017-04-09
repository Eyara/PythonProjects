import telepot
import time
import config

bot = telepot.Bot(config.token)
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    question = config.FindQuestion()

    if content_type == 'text':
        bot.sendMessage(chat_id, question)

TOKEN = config.token  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
