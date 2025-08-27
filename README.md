
# Password Generator

A secure, interactive Python tool for quickly generating passwords with custom settings (length, character types, HIBP check, etc.).

## Features
- Interactive terminal menu for all parameters
- Generate multiple passwords at once
- Optional HIBP leak check ("Have I Been Pwned")
- Easy to use via double-click or command line

## Requirements
- Python 3.7 or newer
- Packages: `requests` (argparse is included in Python 3.2+)

## Install dependencies

Install the required package with:

```
pip install requests
```

## Usage

1. Start the script by double-clicking or in the terminal:

```
python passwort_generator.py
```

2. Follow the menu instructions and select your options.

3. The generated passwords will be displayed and can be copied easily.


## Installing all requirements from requirements.txt

If you want to install all dependencies at once, run:

```
pip install -r requirements.txt
```

---

## Notes
- HIBP check requires an internet connection.
- Passwords are not saved.
- The script works on Windows, Linux, and macOS.
