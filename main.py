import dataclasses
import time
import pandas as pd
from entry_generator import generate_entry
from publisher.pubsub_publisher import publish_message_to_pubsub
from utils.client_ids_generator import shuffle_active_clients_flags


NUMBER_OF_DAYS_TO_UPDATE_ACTIVE_FLAG = 31
NUMBER_OF_SECS_TO_UPDATE_ACTIVE_FLAG = NUMBER_OF_DAYS_TO_UPDATE_ACTIVE_FLAG * 86400
LAST_ACTIVE_FLAG_UPDATE = int(time.time())

all_clients = pd.read_csv('resources/client_ids.csv', header=0)


def update_active_clients_flags():
    global LAST_ACTIVE_FLAG_UPDATE
    if int(time.time()) > LAST_ACTIVE_FLAG_UPDATE + NUMBER_OF_SECS_TO_UPDATE_ACTIVE_FLAG:
        print("updating active clients flags...")
        all_clients["active_flag"] = shuffle_active_clients_flags(all_clients["active_flag"].tolist())
        LAST_ACTIVE_FLAG_UPDATE = time.time()


if __name__ == '__main__':
    print("Program started with success!", flush=True)
    while True:
        update_active_clients_flags()
        entry = generate_entry(all_clients)
        print(f"New entry generated! {dataclasses.asdict(entry)}", flush=True)
        if entry is not None:
            publish_message_to_pubsub(dataclasses.asdict(entry))
            time.sleep(60)
