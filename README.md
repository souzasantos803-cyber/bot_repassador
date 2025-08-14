# 🤖 Bot Repassador

Este bot do Telegram repassa mensagens de usuários ou grupos para destinos configurados.

---

## 🚀 Deploy no Railway

Clique no botão abaixo para implantar automaticamente no [Railway](https://railway.app):

[![Implantar na ferrovia](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/souzasantos803-cyber/bot_repassador&envs=TOKEN,DESTINOS,USUARIOS_IGNORADOS,TIPO_PERMITIDOS&TOKENDesc=Token%20do%20bot%20do%20Telegram&DESTINOSDesc=IDs%20dos%20destinos%20(separados%20por%20v%C3%ADrgula)&USUARIOS_IGNORADOSDesc=IDs%20dos%20usu%C3%A1rios%20para%20ignorar%20(separados%20por%20v%C3%ADrgula)&TIPO_PERMITIDOSDesc=Tipos%20de%20mensagem%20permitidos%20(ex:%20texto,%20%C3%A1udio,%20etc))

---

## 🔧 Variáveis de Ambiente

- `TOKEN` → Token do bot do Telegram (fornecido pelo [BotFather](https://t.me/BotFather))
- `DESTINOS` → IDs de chat ou grupos para onde repassar mensagens (separados por vírgula)
- `USUARIOS_IGNORADOS` → IDs de usuários que serão ignorados (opcional)
- `TIPO_PERMITIDOS` → Tipos de mensagens permitidas (ex.: `texto,audio,video`)

---

## 💻 Rodar Localmente

```bash
pip install python-telegram-bot==20.3 python-dotenv
python bot_repassador.py
