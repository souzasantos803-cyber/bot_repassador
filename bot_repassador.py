import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Carregar configurações do .env ou variáveis do Railway
load_dotenv()

TOKEN = os.getenv("TOKEN")
DESTINOS = [int(x.strip()) for x in os.getenv("DESTINOS", "").split(",") if x.strip()]
USUARIOS_IGNORAR = [int(x.strip()) for x in os.getenv("USUARIOS_IGNORAR", "").split(",") if x.strip()]
TIPO_PERMITIDO = os.getenv("TIPO_PERMITIDO", "todos").lower()

async def repassar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    user_id = update.message.from_user.id

    # Ignorar usuários bloqueados
    if user_id in USUARIOS_IGNORAR:
        return

    # Filtrar por tipo de mensagem
    if TIPO_PERMITIDO == "texto" and not update.message.text:
        return
    if TIPO_PERMITIDO == "mídia" and update.message.text:
        return

    # Repassar para todos os destinos
    for destino in DESTINOS:
        try:
            await update.message.forward(chat_id=destino)
        except Exception as e:
            print(f"Erro ao repassar para {destino}: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot de repasse ativo!")

def main():
    if not TOKEN:
        raise ValueError("⚠️ TOKEN do bot não foi encontrado. Configure nas variáveis de ambiente.")

    app = ApplicationBuilder().token(TOKEN).build()

    # Comando /start
    app.add_handler(MessageHandler(filters.COMMAND, start))

    # Repassar tudo que não seja comando
    app.add_handler(MessageHandler(filters.ALL, repassar))

    print("Bot rodando no Railway...")
    app.run_polling()

if __name__ == "__main__":
    main()
