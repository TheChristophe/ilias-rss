# ILIAS RSS Mailer

RSS -> Mail client made for receiving [ILIAS](https://github.com/ILIAS-eLearning/ILIAS) RSS notifications.

The RSS feed of the [KIT](https://www.kit.edu/) ILIAS got so slow that the browser extension client I used refused to parse it, and I couldn't find a nice alternative.
So I wrote this.

How to use:
1. Copy `config.ini.example` to `config.ini` and fill in the fields
2. (Optional) Set up venv `python -m venv venv`, `. ./venv/bin/activate`
3. Install requirements `pip install -r requirements.txt`
4. Run with `python main.py`, optionally in tmux or in a service

This application only produces output when the RSS is unavailable.
