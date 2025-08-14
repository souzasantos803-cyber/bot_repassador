# Bot de Repassar Mensagens do Telegram

Este bot repassa mensagens de um grupo/canal do Telegram para outros destinos automaticamente.

## 🚀 Como usar no Railway

1. Crie uma conta no [Railway](https://railway.app/).
2. Clique no botão abaixo para fazer o deploy:

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=SEU_REPOSITORIO_AQUI&envs=TOKEN,DESTINOS,USUARIOS_IGNORAR,TIPO_PERMITIDO&desc=Token+do+bot+do+Telegram+e+IDs+dos+destinos+separados+por+vírgula&USUARIOS_IGNORAR=IDs+dos+usuários+para+ignorar&TIPO_PERMITIDO=Tipos+permitidos+(ex:+Podem+ser+%27todos%27+ou+%27texto%27))

---

## 🌱 Variáveis de Ambiente no Railway

- TOKEN: Token do bot fornecido pelo BotFather.
- DESTINOS: IDs de destino separados por vírgula.
- USUARIOS_IGNORAR: IDs de usuários que serão ignorados.
- TIPO_PERMITIDO: Tipos de mensagens permitidas (ex.: todos, `texto`).
