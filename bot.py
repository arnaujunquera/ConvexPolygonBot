from telegram import Update
from antlr4 import *
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, Dispatcher, MessageHandler
from cl.PolygonLexer import PolygonLexer
from cl.PolygonParser import PolygonParser
from cl.EvalPolygon import EvalPolygon


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hola {update.effective_user.first_name}!')
    update.message.reply_text(f'Benvingut al Convex Polygon Bot! Escriu /instructions per veure totes les comandes que pots usar en aquest bot.')
    visitor.cleanDictionary()


def documentation(update: Update, context: CallbackContext) -> None:
    msg = 'Pots consultar la documentació del projecte aquí: https://github.com/arnaujunquera/ConvexPolygonBot'
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(msg))


def author(update: Update, context: CallbackContext) -> None:
    msg = 'Projecte creat per Arnau Junquera Orozco - arnau.junquera@estudiantat.upc.edu'
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(msg))


def savedPolygons(update: Update, context: CallbackContext) -> None:
    msg = visitor.getPolygons()
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(msg))


def instructions(update: Update, context: CallbackContext) -> None:
    msg = '/start - Inicialitza el bot.\n'
    msg += '/instructions - Proporciona informació sobre les comandes del bot.\n'
    msg += '/documentation - Proporciona la documentació del projecte.\n'
    msg += '/author - Autor del projecte.\n'
    msg += '/savedPolygons - Mostra tots els polígons desats.\n'
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(msg))


def readExpr(update, context):
    # Method executed when the recieved message is a text and not a command.
    # The message is sended to EvalPolygon as a expression
    message = InputStream(update.message.text)

    try:
        lexer = PolygonLexer(message)
        token_stream = CommonTokenStream(lexer)
        parser = PolygonParser(token_stream)
        tree = parser.root()
        polygon = visitor.visit(tree)
        reply = polygon
        if type(polygon) == str and polygon[-4:] == ".png":
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(polygon, 'rb'))
            context.bot.send_message(chat_id=update.effective_chat.id, text=str('Imatge desada: ' + polygon))

        elif reply is not None:
            context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text=str('Entrada invàlida.'))

# token
updater = Updater('1447892047:AAFKjJQrun4TeX7v6JyYllcMKcFSP3TF0F0')
# visitor
visitor = EvalPolygon()
# handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('instructions', instructions))
updater.dispatcher.add_handler(CommandHandler('documentation', documentation))
updater.dispatcher.add_handler(CommandHandler('author', author))
updater.dispatcher.add_handler(CommandHandler('savedPolygons', savedPolygons))
updater.dispatcher.add_handler(MessageHandler(Filters.text, readExpr))

updater.start_polling()
updater.idle()
