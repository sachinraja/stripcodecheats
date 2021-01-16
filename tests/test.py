import os
from dotenv import load_dotenv

import sys
sys.path.append(os.path.abspath("../stripcodecheats"))
import stripcodecheats

load_dotenv()

GITHUB_USERNAME = os.environ["GITHUB_USERNAME"]
GITHUB_PASSWORD = os.environ["GITHUB_PASSWORD"]

# optional
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

stripcodecheats.start(GITHUB_USERNAME, GITHUB_PASSWORD, github_token=GITHUB_TOKEN, executable_path="drivers/chromedriver.exe", iteration_count=5)