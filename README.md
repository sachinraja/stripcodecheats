# stripcodecheats
Cheats for the game [StripCode](https://stripcode.dev/) by [benawad](https://github.com/benawad) utilizing the selenium library.

## Installation
All steps are required.

  1. Selenium - [Download a chromedriver](https://chromedriver.chromium.org/) and put it in the directory for this repository.

  2. [PyPi](https://pypi.org/project/stripcodecheats/) - Run `pip install stripcodecheats` to install the module for this and its dependencies.

## Setup
```py
import os
from dotenv import load_dotenv
import stripcodecheats

load_dotenv()

GITHUB_USERNAME = os.environ["GITHUB_USERNAME"]
GITHUB_PASSWORD = os.environ["GITHUB_PASSWORD"]

# optional
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

stripcodecheats.start(GITHUB_USERNAME, GITHUB_PASSWORD, github_token=GITHUB_TOKEN, executable_path="drivers/chromedriver.exe", iteration_count=10)
```

Your github username and password are necessary because StripCode will ask for your github account details when connecting for the first time. If you do not provide a separate token, this will also be used to request information from the GitHub API.

## How It Works
[Selenium](https://github.com/SeleniumHQ/selenium) is used for automatically handling the interactions with the page. It scrapes the buttons from the page and gets the repository ids from them. These are then passed to a function that queries the GitHub API for their trees. The trees are iterated over to check if a filename matches, and the answer with the match is clicked by selenium. All of the filenames with an extension matching one of the valid languages for each repository are cached to limit the amount of requests made to the GitHub API. These are then dumped into a file by [pickle](https://docs.python.org/3/library/pickle.html) when the program finishes and loaded back in when the program is run.