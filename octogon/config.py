"""
Octogon Panel Constants
"""
import os
import json
import logging
from typing import Optional
from colorama import Fore, Style

cwd = os.getcwd()

logging.addLevelName(logging.WARNING, "WARN")
logging.addLevelName(logging.ERROR, "ERR")
logging.addLevelName(logging.CRITICAL, "CRIT")

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(
    logging.Formatter(
        str(
            Fore.LIGHTBLACK_EX
            + "["
            + Fore.GREEN
            + "%(name)s"
            + Fore.LIGHTBLACK_EX
            + "]"
        ).expandtabs(10)
        + "["
        + Fore.BLUE
        + "%(levelname).1s"
        + Fore.LIGHTBLACK_EX
        + "] "
        + Style.RESET_ALL
        + "%(message)s"
    )
)


# alias for print()
def get_print_fn(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(ch)

    return logger.info


print = get_print_fn("octogon")


CONFIG_PATH = "config.json"


def load_config():
    """Load constants from the config file."""

    print("loading config...")
    try:
        conf = json.load(open(CONFIG_PATH))
    except FileNotFoundError:
        # write a default config
        conf = {
            "style_path": "style/",
            "template_path": "templates/",
            "sb_path": "scoreboard.json",
            "smashgg_api_key": "",
            "smashgg_tourny_slug": "",
            "smashgg_event_id": "",
        }
        with open(CONFIG_PATH, "w") as f:
            json.dump(conf, f, ensure_ascii=False, indent=4)
            print("created default config")

    print("config loaded!")

    global config
    config = Config(conf)


class Config:
    def __init__(self, data: dict):
        self.data = data

        # location of .scss files
        self.STYLE_PATH = data["style_path"]
        # location of jinja2 templates
        self.TEMPLATE_PATH = data["template_path"]
        # location of scoreboard data
        self.SB_DATA_PATH = data["sb_path"]

        self.SMASHGG_API_KEY = data["smashgg_api_key"]
        self.SMASHGG_TOURNY_SLUG = data["smashgg_tourny_slug"]
        self.SMASHGG_EVENT_ID = data["smashgg_event_id"]


config: Optional[Config] = None