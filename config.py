from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgAQ0zM39w-pQD7GcvgV9ZbBe_2GBLQTPAzLf_8UQrlAEJCZx_R_N7lXghw_bjl1sf8j5wx8o-m9iJkz0E4IvLaDvwVvLhkcovATL0a-dG89dAy33w2QWu_GKVrpnER0QYBqr3loUbl699HQi_PibWgaOG2ZxEWM08-eALUHf5ko5WTnYEKMdoCzoHgorKbBdi_3uP57edApEuEreiZpLRBCtzhkPC8hnOSRKQ7nslp3Ev28neZrUsSxQD-tnhfTsOI2_A8ifhSKV6u76jnila0bX-UOEL6LeXSRf8LpfQi7qYhDtiBIBxJcjSTqRgDQNslhffWeaeoyYv4zE96cupLTAAAAAUSeCNcA")
BOT_TOKEN = getenv("BOT_TOKEN", "5510964177:AAGkFJSZMcHmV0cpI1M-J1zhF5VCMIB7YuA")
BOT_NAME = getenv("BOT_NAME", "SOA MUSİC") 
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "soamusicbot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
