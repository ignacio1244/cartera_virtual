from telegram.ext import  Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, Requests , Schedule

INPUT_TEXT = 0

def start(update, context):
    update.message.reply_text("hola hola")

def pago(update, context):
    update.message.reply_text("el saldo actual es: ")

    return INPUT_TEXT

def input_text(update, context):
    text = update.message.text
    print(text)

if __name__ == "__main__":
    Updater = Updater(token="1874222275:AAHJu-ptKk8yacJ8V-jR4FKUF6dvSylugXk", use_context = True )

    dp = Updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler("pago", pago)
        ],
        states={
            INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
        },         
        fallbacks=[]
    ))

    Updater.start_polling()
    Updater.idle()    


    asdasd
asdasdasdasda