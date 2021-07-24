from telegram.ext import  Updater, CommandHandler

def start(update, context):
    update.message.reply_text("hola hola")


if __name__ == "__main__":
    Updater = Updater(token="1874222275:AAHJu-ptKk8yacJ8V-jR4FKUF6dvSylugXk", use_context = True )

    dp = Updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    Updater.start_polling()
    Updater.idle()    
    UWU
    uwu de permiso
