from typing import cast

from dotenv import dotenv_values, find_dotenv

env_path = find_dotenv()

config = dotenv_values(env_path)


class Settings:
    PATH: str = cast(str, config["PATH"])
    SECRET_API: str = cast(str, config["SECRET_API"])
    LOGIN: str = cast(str, config["LOGIN"])
    PASSWORD: str = cast(str, config["PASSWORD"])


settings = Settings()
