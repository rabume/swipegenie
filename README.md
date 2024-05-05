# ✨️ SwipeGenie

SwipeGenie is a tool that automates your dating life on Tinder. It uses ADB to automate the interactions with the app on your Android Phone. Additionally, it utilizes the Ollama API validate your potential matches with the Llava model against your preferences.

Inspired by [T-Man](https://github.com/dcostersabin/T-Man).

## ⚡️ Requirements

-   Python => 3.11.4
-   Ollama => running llava model
-   Android Phone => with USB debugging enabled

## 🧑‍💻 Development

Copy the `.env.example` file to `.env` and fill in the required values.

```bash
cp .env.example .env
```

Run the following commands to install the required dependencies.

```bash
# Install python version (3.11.4)
pyenv install

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Fish specific way to activate the virtual environment
source .venv/bin/activate.fish

# Install the requirements
pip install -r requirements.txt
```

## 🚀️ Usage

> Requires that the dependencies are installed. (See above)

1. Connect your Android phone to your computer.
2. Enable USB debugging on your phone.
3. Start the ollama server.
4. Run the following command to start the application:

```bash
python main.py --PIN ****
```
