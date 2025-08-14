# Bot de Repassar Mensagens do Telegram

Este bot repassa mensagens de um grupo/canal do Telegram para outros destinos automaticamente.

---

## 🚀 Como usar no Railway

1. Crie uma conta no [Railway](https://railway.app/).
2. Clique no botão abaixo para fazer o deploy:

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/souzasantos803-cyber/bot_repassador&envs=TOKEN,DESTINOS,USUARIOS_IGNORA,TIPO_PERMITIDO&TOKENDesc=Token%20do%20bot%20do%20Telegram&DESTINOSDesc=IDs%20dos%20destinos%20separados%20por%20v%C3%ADrgula&USUARIOS_IGNORADesc=IDs%20dos%20usu%C3%A1rios%20a%20ignorar%20separados%20por%20v%C3%ADrgula&TIPO_PERMITIDODesc=Tipos%20permitidos%20de%20mensagem)

---

### ⚙️ Variáveis de Ambiente no Railway

- TOKEN → Token do bot fornecido pelo BotFather.
- DESTINOS → IDs dos destinos separados por vírgula.
- USUARIOS_IGNORA → IDs dos usuários que serão ignorados.
- TIPO_PERMITIDO → Tipos de mensagens permitidas (ex.: text, photo, `video`).

---

📌 Observação:  
- Adicione o bot como administrador no grupo/canal para que ele consiga ler e repassar as mensagens.  
- Caso queira testar localmente antes de colocar no Railway, você pode clonar este repositório e executar com python bot.py após configurar as variáveis no .env.
