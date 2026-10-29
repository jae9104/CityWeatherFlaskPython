# What Should I Wear?

A simple Flask web application that checks the current temperature in a city
and recommends what to wear.

## Requirements

- Python 3.10 or later
- An API key from [WeatherAPI](https://www.weatherapi.com/)

## Installation

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   On Windows, activate the environment with:

   ```powershell
   .venv\Scripts\activate
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create the local environment file from the template:

   ```bash
   cp .env.example .env
   ```

4. Open `.env` and replace `your_weatherapi_key_here` with your WeatherAPI
   key. The `.env` file is excluded by `.gitignore` and must not be committed
   to the repository.

## Running the application

```bash
python app.py
```

Then open <http://127.0.0.1:5000> in your browser.

The application runs in `debug` mode for local development. Before deploying
it to production, use a WSGI server and configure debug mode appropriately for
the environment.

## Project structure

```text
.
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Security

- Do not share `.env` or copy the API key into the source code.
- `.gitignore` prevents `.env` and generated files from being included in Git
  commits, but it cannot prevent someone from manually uploading those files
  outside Git.
- If an API key has already been published or shared accidentally, revoke it
  and generate a new one through WeatherAPI.
