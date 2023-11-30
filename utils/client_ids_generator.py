import pandas as pd
import random
import string

NUMBER_OF_CLIENTS = 50000


def generate_client_id(existing_ids):
    while True:
        client_id = 'CL' + ''.join(random.choice(string.digits) for _ in range(6))
        if client_id not in existing_ids:
            return client_id


client_ids = []


def generate_client_ids():
    while len(client_ids) < NUMBER_OF_CLIENTS:
        new_client_id = generate_client_id(client_ids)
        client_ids.append(new_client_id)

    active_client_flag = random.choices([True, False], weights=[NUMBER_OF_CLIENTS, int(NUMBER_OF_CLIENTS / 12)],
                                        k=NUMBER_OF_CLIENTS)

    df = pd.DataFrame(data={'client_id': client_ids, 'active_flag': active_client_flag})

    csv_filename = '../resources/client_ids.csv'
    df.to_csv(csv_filename, index=False, header=True)
    print(f'CSV file "{csv_filename}" with {NUMBER_OF_CLIENTS} entries has been created.')


def shuffle_active_clients_flags(active_flags_list):
    random.shuffle(active_flags_list)
    return active_flags_list
