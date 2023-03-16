from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from settings import MESSAGES, TELEGRAM_BOT_API_TOKEN

# STATES
REG_WAITING_PIN, AUTH_WAITING_PIN = range(2)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = MESSAGES.get("START")
    await update.message.reply_text(message)


async def reg_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    message = MESSAGES.get("CREATE_PIN")
    await update.message.reply_text(message)
    return REG_WAITING_PIN


async def auth_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    message = MESSAGES.get("ENTER_PIN")
    await update.message.reply_text(message)
    return AUTH_WAITING_PIN


async def reg_entering_pin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    pin = update.message.text
    message = MESSAGES.get("REG_OK")
    await update.message.reply_text(message)
    return ConversationHandler.END


async def auth_entering_pin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    pin = update.message.text
    message = MESSAGES.get("AUTH_OK")
    await update.message.reply_text(message)
    return ConversationHandler.END


app = ApplicationBuilder().token(TELEGRAM_BOT_API_TOKEN).build()

reg_conv_handler = ConversationHandler(
    entry_points=[CommandHandler("reg", reg_command)],
    states={
        REG_WAITING_PIN: [
            MessageHandler(filters.Regex("^[0-9]{6}$"), reg_entering_pin),
            CommandHandler("start", start),
        ],
    },
    fallbacks=[],
)
auth_conv_handler = ConversationHandler(
    entry_points=[CommandHandler("auth", auth_command)],
    states={
        AUTH_WAITING_PIN: [
            MessageHandler(filters.Regex("^[0-9]{6}$"), auth_entering_pin),
            CommandHandler("start", start),
        ],
    },
    fallbacks=[],
)
app.add_handler(reg_conv_handler)
app.add_handler(auth_conv_handler)
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("reg", reg_command))
app.add_handler(CommandHandler("auth", auth_command))

app.run_polling()
