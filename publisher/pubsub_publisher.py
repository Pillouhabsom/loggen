import json
import os

from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
project_ids = os.getenv("PUBSUB_PROJECT_IDS").split("/")
topic_ids = os.getenv("PUBSUB_TOPIC_IDS").split("/")
topic_names = []
for i in range(len(project_ids)):
    topic_names.append('projects/{project_id}/topics/{topic}'.format(
        project_id=project_ids[i],
        topic=topic_ids[i],
    ))

def publish_message_to_pubsub(entry):
    data = json.dumps(entry).encode("utf-8")
    for j in range(len(topic_names)):
        future = publisher.publish(topic_names[j], data)
        print(f'entry published in topic: {topic_names[j]}', flush=True)
