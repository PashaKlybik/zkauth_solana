import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_API_TOKEN = os.environ.get("TELEGRAM_BOT_API_TOKEN")

MESSAGES = {
    "START": """Hello there! Thank you for choosing our zk-auth for Solana authentication. 
To get started, please enter /reg and **PIN**. 
We're here to ensure a smooth authentication process for you.""",
    "REG_OK": """Congratulations! You have successfully registered. Welcome aboard!
To go futher type /auth **PIN**""",
    "REG_FAIL": """We're sorry, but your registration has failed. Please try again and use some other **PIN**""",
    "AUTH_OK": """You have successfully logged in right in smart contract in Solana blockchain just with your Tegeram ID and PIN""",
    "AUTH_FAIL": """Sorry, we were unable to log you in. Please check your login credentials and try again""",
    "CREATE_PIN": "Please, enter your PIN",
    "ENTER_PIN": "Please, enter your PIN",
}
