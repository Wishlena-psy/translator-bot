# 🌐 Деловой переводчик-бот

Telegram-бот для деловых переговоров, встреч и переписки на разных языках.

**Рабочий пример:** [@translate_Wishlena_bot](https://t.me/translate_Wishlena_bot)

---

## Что умеет

| Возможность | Описание |
|---|---|
| 🇷🇺🇨🇳🇬🇧🇮🇱 4 языка | Русский, Китайский, Английский, Иврит — в любую сторону |
| ✍️ Текст | Напиши — получи перевод |
| 🎤 Голосовые | Расшифровка + перевод + голосовой ответ |
| 🎵 Аудиофайлы | mp3, m4a, wav, ogg — длинные встречи целиком |
| 📷 Фото с текстом | Меню, договор, вывеска — прочитает и переведёт |
| 🗣 Живой диалог | Компактный режим: только перевод, голос автоматически |
| 🌐 UI на языке пользователя | Интерфейс переключается на родной язык автоматически |
| 💼 Деловой / 💬 Обычный стиль | Выбирается в настройках |
| 📋 Согласие 152-ФЗ | Автоматически при первом запуске |
| 🔁 White-label | Один сервер — много ботов для разных клиентов |

---

## Быстрый старт

### 1. Установить зависимости

```bash
# Node.js 20
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs ffmpeg

# Python-библиотеки
pip install faster-whisper edge-tts --break-system-packages
```

### 2. Клонировать и установить

```bash
git clone https://github.com/YOUR/translator-bot.git
cd translator-bot
npm install
```

### 3. Настроить

```bash
cp env.example tr.env
nano tr.env   # вписать BOT_TOKEN и OWNER_ID
```

### 4. Запустить

```bash
# Напрямую (для теста)
node bot.js

# Через PM2 (для VPS, постоянная работа)
npm install -g pm2
pm2 start start.sh --name translator-bot
pm2 save
pm2 startup   # автозапуск при перезагрузке сервера
```

---

## Переменные окружения

Создай файл `tr.env` (скопировав `env.example`):

```env
BOT_TOKEN=     # токен от @BotFather
OWNER_ID=      # ваш Telegram ID (от @userinfobot)
OPERATOR_NAME= # ИП / ООО для 152-ФЗ
OPERATOR_INN=  # ИНН
```

Полный список — в файле `env.example`.

---

## White-label: бот для клиента

Один сервер → много ботов. Каждый бот = своя папка + свой `tr.env`.

```bash
cp -r translator-bot/ translator-client/
cd translator-client/
nano tr.env  # токен клиента + TR_STATE_FILE=./state.json
pm2 start start.sh --name translator-client
```

---

## Архитектура

```
bot.js          — основной бот (~1600 строк, Node.js + Grammy)
transcribe.py   — расшифровка аудио (Python + faster-whisper)
start.sh        — точка входа (загружает env, запускает node)
env.example     — шаблон переменных
state.json      — профили пользователей (создаётся автоматически)
```

**Стек:**
- [Grammy](https://grammy.dev) — Telegram Bot Framework
- [Claude API](https://anthropic.com) — перевод текста и чтение фото
- [edge-tts](https://github.com/rany2/edge-tts) — голосовые ответы (Microsoft Neural TTS, бесплатно)
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) — расшифровка аудио локально
- [OpenAI Whisper API](https://platform.openai.com/docs/guides/speech-to-text) — быстрая расшифровка (опционально)

---

## Команды

| Команда | Действие |
|---|---|
| `/start` | Начало, онбординг |
| `/menu` | Настройки |
| `/swap` | Поменять языки местами |
| `/voice` | Голосовой ответ вкл/выкл |
| `/live` | Живой диалог вкл/выкл |
| `/help` | Справка |

---

## Требования

- VPS Ubuntu 20.04+ (минимум 1 ГБ RAM — для faster-whisper)
- Node.js 20+
- Python 3.10+
- ffmpeg
- Claude API (через Anthropic API key или Claude Max подписку)

---

## Лицензия

MIT — используй, модифицируй, продавай клиентам.
