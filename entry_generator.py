import random
import time
import pandas as pd
from pandas import DataFrame

from login_entry import DeviceType, Browser, OS, LoginEntry

INVALID_LOGIN_DATE_PROBABILITY = 0.1
NULL_CLIENT_ID_PROBABILITY = 0.05
ONE_DAY_IN_SECONDS = 86400.


def pick_random_client(df: pd.DataFrame):
    client_id = None
    if random.random() > NULL_CLIENT_ID_PROBABILITY:
        index = random.randint(0, len(df.index) - 1)
        return df['client_id'].iloc[index]
    return client_id


def get_login_timestamp():
    login_timestamp = time.time()
    if random.random() < INVALID_LOGIN_DATE_PROBABILITY:
        login_timestamp = time.time() + ONE_DAY_IN_SECONDS
    return login_timestamp


def pick_browser(device_type: str):
    if device_type.__eq__(DeviceType.DESKTOP.value):
        return random.choices([Browser.CHROME.value, Browser.FIREFOX.value], weights=[1, 1], k=1)[0]
    else:
        return random.choices([e.value for e in Browser], weights=[2, 2, 6], k=1)[0]


def pick_os(device_type):
    if device_type.__eq__(DeviceType.DESKTOP.value):
        return random.choices([OS.LINUX.value, OS.MAC_OS.value, OS.WINDOWS.value], weights=[1, 3, 2], k=1)[0]
    else:
        return random.choices([OS.ANDROID.value, OS.IOS.value], weights=[4, 6], k=1)[0]


def generate_entry(all_clients: DataFrame):
    random.seed(int(time.time()))
    client_id = pick_random_client(all_clients)
    if client_id is not None:
        is_client_active = all_clients[all_clients["client_id"] == client_id]["active_flag"].iloc[0]
        if not is_client_active:
            pass
    login_timestamp = get_login_timestamp()
    device_type = random.choices([e.value for e in DeviceType], weights=[10, 3, 2], k=1)[0]
    browser = pick_browser(device_type)
    os = pick_os(device_type)

    return LoginEntry(client_id, login_timestamp, device_type, browser, os)
