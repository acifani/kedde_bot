import os
import logging
from uuid import uuid4
from string import maketrans

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

intab = "aiotcpq"
outtab = "eeedgbg"
trantab = maketrans(intab, outtab)


def genverde(text):
    return "hehehe " + text.encode('utf-8').translate(trantab) + " hehehe"


def inline_genverde(bot, update):
    query = update.inline_query.query
    results = list()

    results.append(InlineQueryResultArticle(
        id=uuid4(),
        title="Genverde en keddese",
        input_message_content=InputTextMessageContent(genverde(query))))

    update.inline_query.answer(results)


def start(bot, update):
    update.message.reply_text('Hehehe')


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    logger.info("Kit_Token: " + os.getenv('KIT_TOKEN'))
    updater = Updater(os.getenv('KIT_TOKEN'))
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(InlineQueryHandler(inline_genverde))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
