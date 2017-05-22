# kedde_bot

## Setup
### Requirements
* Either Docker or Python3 (virtualenv recommended)
* Telegram Bot API, ask [BotFather](https://telegram.me/BotFather)

#### Virtual Env
```
$ virtualenv venv
$ source venv/bin/activate
$(venv) pip install -r requirements.txt
```

#### Docker
```
$ docker build -t kedde_bot:latest .
```

## Run

#### Virtual Env
```
$(venv) export KIT_TOKEN=<telegram_bot_token>
$(venv) python kedde_bot.py
```

#### Docker
```
$ docker run -d -e "KIT_TOKEN=<telegram_bot_token>" kedde_bot:latest
```
