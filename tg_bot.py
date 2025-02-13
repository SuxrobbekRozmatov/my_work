import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from youtube_search import YoutubeSearch

# Loggingni yoqish
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


# Start komandasi
async def start(update: Update, context):
    await update.message.reply_text('Salom! Musiqa izlash uchun nomini yozing.')


# Musiqa qidirish
async def search_music(update: Update, context):
    query = update.message.text
    try:
        # YouTube'dan qidirish
        results = YoutubeSearch(query, max_results=5).to_dict()

        if results:
            response = "Topilgan musiqalar:\n"
            for i, video in enumerate(results):
                title = video['title']
                url = f"https://www.youtube.com{video['url_suffix']}"
                response += f"{i + 1}. {title}\n{url}\n\n"
            await update.message.reply_text(response)
        else:
            await update.message.reply_text("Musiqa topilmadi. Iltimos, yana urinib ko'ring.")
    except Exception as e:
        # Xatolikni logga yozish
        logger.error(f"Xatolik yuz berdi: {e}")
        await update.message.reply_text("Musiqa qidirishda xatolik yuz berdi. Iltimos, keyinroq urinib ko'ring.")


# Botni ishga tushurish
def main():
    # Telegram bot token
    TOKEN = 'bot_tokeni'

    # Application yaratish
    application = Application.builder().token(TOKEN).build()

    # Handlerlar
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_music))

    # Botni ishga tushurish
    application.run_polling()


if __name__ == '__main__':
    main()