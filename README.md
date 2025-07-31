# Columbia Housing Availability Telegram Bot

Checks if "517 W 121st St" is available on Columbia Housing portal and sends a Telegram message when it is.

## Setup

1. Clone the repo
2. Create a `.env` file with your Telegram credentials:

```
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_id
```

3. Run the login script and save cookies:
```bash
python login_and_save_cookies.py
```

4. Start the bot:
```bash
python housing_checker.py
```

## Notes

- Requires manual login (DUO) once to generate `cookies.pkl`
- Uses Selenium + headless Chrome
