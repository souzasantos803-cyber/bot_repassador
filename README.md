# Bot de Repassar Mensagens do Telegram

Este bot repassa mensagens de um grupo/canal do Telegram para outros destinos automaticamente.

## 🚀 Como usar no Railway

1. Crie conta em [Railway](https://railway.app/)
2. Clique no botão abaixo para fazer deploy:
   
   [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=SEU_REPOSITORIO_AQUI&envs=TOKEN,DESTINOS,USUARIOS_IGNORAR,TIPO_PERMITIDO&TOKENDesc=Token+do+bot+do+Telegram&DESTINOSDesc=IDs+dos+destinos+separados+por+vírgula&USUARIOS_IGNORARDesc=IDs+dos+usuários+para+ignorar&TIPO_PERMITIDODesc=Pode+ser+%27todos%27%2C+%27texto%27+ou+%27m%C3%ADdia%27)

3. Configure as variáveis de ambiente no Railway:
   - `TOKEN` → Token do bot fornecido pelo BotFather
   - `DESTINOS` → IDs dos grupos/canais para repassar mensagens
   - `USUARIOS_IGNORAR` → IDs dos usuários que não quer repassar
   - `TIPO_PERMITIDO` → `todos`, `texto` ou `mídia`

4. Deploy e pronto!

## 💻 Rodar localmente
```bash
pip install python-telegram-bot==20.3 python-dotenv
python bot_repassador.py
```
