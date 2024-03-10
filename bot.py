from config import *
import telebot
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

user_membership_data = {
    "user1": {"plan_validity": True},
    "user2": {"plan_validity": False}
}

chatStr = '' 
def ChatModal(prompt):
    global chatStr
    openai.api_key=OPENAI_KEY
    chatStr += f"Damove: {prompt}\nDamoveBot: "
    response = openai.completions.create(
                model="davinci-002",
                prompt=chatStr,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
    chatStr += f"{response['choices'][0]['text']}"
    return response['choices'][0]['text']

def call_script(update, context):
    user_id = str(update.effective_user.id)
    if user_membership_data.get(user_id, {}).get("plan_validity", false):
        update.message.reply_text(ChatModal("Call command"))
    else:
        update.message.reply_text("Sorry, your membership plan is not active.")

def membership_command(update, context):
    user_id = str(update.effective_user.id)
    if user_membership_data.get(user_id, {}).get("plan_validity", False):
        update.message.reply_text("Your membership plan is active.")
    else:
        update.message.reply_text("Your membership plan is not active.")



# bot=telebot.TeleBot(BOT_API)
# @bot.message_handler(['start'])
        
def start(update, context):
    update.message.reply_text("Hello,  Welcome to Damove OTP Bypass Bot")
# @bot.message_handler()
def chat(message):
    #if message.from_user.id==my_id:
        try:
            reply = ChatModal(message.text)
            bot.reply_to(message,reply)
        except Exception as e:
            print(e)
            bot.reply_to(message,e)
    # else:
    #     print("Someone else tried our bot: ",message.text)
def main():
    updater = Updater(BOT_API, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("membership", membership_command))
    dp.add_handler(CommandHandler("call", call_script))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()