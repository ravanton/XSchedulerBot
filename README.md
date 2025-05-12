# X Scheduler Bot

A Python bot that automatically posts scheduled tweets using the Twitter API v2.

## Features
- Posts quotes from a local SQLite database
- Scheduled via `APScheduler`
- Logs events and errors
- Validates tweet content
- Uses `.env` file for secrets

## Requirements
- Python 3.9+
- Twitter API Bearer Token

## Setup
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Rename `.env.example` to `.env` and fill in your `TWITTER_BEARER_TOKEN`
4. Add your quotes to the SQLite database:
   ```bash
   python load_quotes.py
   ```
5. Run the bot:
   ```bash
   python main.py
   ```

## Directory Structure
```
.
├── main.py
├── utils
│   ├── db.py
│   ├── logger.py
│   ├── twitter_api.py
│   └── validator.py
├── data
│   └── quotes.db
├── .env.example
└── README.md
```

## License
MIT
