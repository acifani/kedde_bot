import os
import re
import logging
from uuid import uuid4
from collections import OrderedDict

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

translation_table = [
    ('c(a|i|o)', 'ghe'),
    ('a|i|o', 'e'),
    ('t', 'd'),
    ('c', 'g'),
    ('p', 'b'),
    ('q', 'g')
]

ordered_translation_table = OrderedDict(translation_table)

def he_factory(n):
    return "he"*n

def genverde(text):
    res = text
    for key, value in ordered_translation_table.items():
        res = re.sub(key, value, res)
    return he_factory(3) + res + he_factory(3)


def inline_genverde(bot, update):
    query = update.inline_query.query
    results = list()

    results.append(InlineQueryResultArticle(
        id=uuid4(),
        title="Genverde",
        description="Genverde el desde en keddese",
        input_message_content=InputTextMessageContent(genverde(query))))

    update.inline_query.answer(results)


def message_genverde(bot, update, args):
    if len(args) <= 0:
        update.message.reply_text("hehehe deve sgrevere guelgese hehehe")
    else:
        query = ' '.join(args)
        update.message.reply_text(genverde(query))


def start(bot, update):
    update.message.reply_text(he_factory(3))


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    logger.info("Kit_Token: " + os.getenv('KIT_TOKEN'))
    updater = Updater(os.getenv('KIT_TOKEN'))
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("kit", message_genverde, pass_args=True))
    dp.add_handler(InlineQueryHandler(inline_genverde))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
