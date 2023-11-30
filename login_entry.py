from dataclasses import dataclass
from enum import Enum
from time import time


class DeviceType(Enum):
    SMARTPHONE = "smartphone"
    TABLET = "tablet"
    DESKTOP = "desktop"


class Browser(Enum):
    CHROME = "Chrome"
    FIREFOX = "Firefox"
    APP = "App"


class OS(Enum):
    ANDROID = "Android"
    IOS = "IOS"
    MAC_OS = "MAC OS"
    WINDOWS = "Windows"
    LINUX = "Linux"


@dataclass
class LoginEntry:
    client_id: str
    login_timestamp: time
    device_type: str
    browser: str
    os: str
