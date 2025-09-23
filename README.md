
# 🤖 Chatbot Telegram

Este projeto apresenta a construção de um chatbot multifuncional para o Telegram, desenvolvido em Python com a biblioteca ``pyTelegramBotAPI``. O objetivo principal é centralizar diversas utilidades e serviços em uma única interface de conversação, oferecendo desde respostas geradas por IA até notícias em tempo real.

O bot foi arquitetado de forma modular, buscando uma estrutura de código limpa e de fácil manutenção, permitindo que novas integrações e funcionalidades sejam adicionadas de maneira simples e escalável.

### Funcionalidades Integradas:

**🤖 Inteligência Artificial com Gemini:**
Integrado diretamente com a API do Google Gemini através da biblioteca ``google-generativeai``. O bot é capaz de manter conversas, responder a perguntas complexas e gerar conteúdo, atuando como um assistente inteligente disponível 24/7.

**📰 Web Scraping de Notícias em Tempo Real:**
Utilizando as bibliotecas ``BeautifulSoup`` e ``requests``, o bot realiza um web scraping no portal de notícias G1 para buscar as 5 manchetes mais recentes. O resultado é entregue instantaneamente no chat, com título e link para a matéria completa.

**🔗 Gerador de QR Code Instantâneo:**
Com a ajuda da biblioteca ``qrcode``, o bot pode gerar um QR Code a partir de qualquer texto ou link enviado pelo usuário, facilitando o compartilhamento de informações de forma rápida e visual.

**🏗️ Arquitetura Focada em Manutenibilidade:**
Apesar da simplicidade aparente de um bot, foi dada atenção especial à arquitetura do software. O código é organizado para separar as responsabilidades de cada serviço, garantindo que o projeto permaneça legível, coeso e fácil de expandir no futuro.
## Rodando localmente

Clone o projeto

```
  git clone https://github.com/LucasVizoto/telegram_bot.git
  cd telegram_bot
```
Crie um ambiente virtual
```
python -m venv venv

source venv/bin/activate   # Linux/MacOS
venv\Scripts\activate      # Windows
```

Instale as dependências

```
  pip install -r requirements.txt
```
---
####
#### 3. Configuração das Chaves (Tokens)

Para que o bot funcione, você precisará de credenciais do Telegram e do Google AI.

* ``Token do Bot (Telegram)``
Inicie uma conversa com o @BotFather no Telegram. 

Digite o comando /newbot e siga as instruções, definindo um nome e um username para o seu bot. 

Ao final, o BotFather fornecerá um token de acesso. Guarde este token.

####
* ``Chat ID (Telegram)``

O CHAT_ID é o identificador único da conversa para onde o bot enviará mensagens.

Para uso pessoal (você conversando com o bot):

Inicie uma conversa com o bot @userinfobot.

Ele mostrará seu ID de usuário. Este é o seu CHAT_ID.

* ``Para uso em um grupo:``

Crie um novo grupo no Telegram e adicione o seu bot como membro.

Envie qualquer mensagem no grupo.

Acesse a seguinte URL no seu navegador, substituindo <SEU_TOKEN> pelo token do seu bot:

``https://api.telegram.org/bot<SEU_TOKEN>/getUpdates``

Procure pela chave "chat", e dentro dela, pela chave "id". O valor (geralmente um número negativo) é o CHAT_ID do seu grupo.

*  ``Chave da API (Google Gemini)``

Acesse o Google AI Studio.

Faça login com sua conta Google e clique em "Create API key".

Copie e guarde a chave gerada.

* ``Configurar Variáveis de Ambiente``

Com todas as chaves em mãos, configure o arquivo de ambiente.

Renomeie o arquivo .env.example para .env.

Abra o arquivo .env e preencha com as credenciais que você obteve nos passos anteriores.

####

* ``Inicie o servidor``

```
  python run.py
```
####

## Commands


* Retorna uma mesagem de ajuda

```
  /help
```
**Retorno Esperado:**

Olá, este é um bot puramente para testes com a finalidade de
desenvolver meu conhecimento técnico sobre a integração com o Telegram.
Fique a vontade para explorar qualque um dos comandos existentes.
Para mais detalhes, digite " / " e verifique a listagem.

####
* Retorna as 5 notícias mais recentes do G1 com nome e link da matéria.

```
  /noticias
```

**Retorno Esperado:**

<img src="https://i.imgur.com/Ni1pwzf.png" alt='news_image'/>

####
* Retorna um QRCode com o valor que foi digitado após o comando.

```
  /qrcode meu-qrcode
```

**Retorno Esperado:**

<img src="https://i.imgur.com/aQcuNCY.png" alt='qrcode_image'/>

####
* Retorna a resposta de sua integração com o Google Gemini.
```
  /ai minha pergunta
```

**Retorno Esperado:**

<img src="https://i.imgur.com/4NAagVz.png" alt='qrcode_image'/>

## 🔗 Links
Você também pode me encontrar em:

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lucasvizoto)
[![gmail](https://img.shields.io/badge/Email-1DA1F2?style=for-the-badge&logo=gmail&logoColor=white&color=red)](mailto:lucasvizoto364@gmail.com)

