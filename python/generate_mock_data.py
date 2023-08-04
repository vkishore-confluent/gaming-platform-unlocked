from confluent_kafka import Producer
import datetime
import random
import time
import json
import fastavro

# Avro schema for the value
avro_schema = {
    "type": "record",
    "name": "txn_schema",
    "fields": [
        {"name": "id", "type": "string"},
        {"name": "user_id", "type": "string"},
        {"name": "txn_type", "type": "string"},
        {"name": "txn_timestamp", "type": "string"},
        {"name": "total_sales", "type": "int"},
        {"name": "currency", "type": "string"},
        {"name": "items", "type": {"type": "array", "items": "string"}}
        # Add more fields as needed
    ]
}

# Function to generate mock data
def generate_mock_data():
    txn_id = "txn" + str(random.randint(1, 1000))
    user_id = "user" + str(random.randint(1, 100))
    txn_type = random.choice(["purchase", "refund"])
    txn_timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    total_sales = random.randint(1, 100)
    currency = random.choice(["USD", "EUR", "GBP"])
    items = random.sample(["coins", "game_cash", "item1", "item2", "item3"], random.randint(1, 3))

    data = {
        "id": txn_id,
        "user_id": user_id,
        "txn_type": txn_type,
        "txn_timestamp": txn_timestamp,
        "total_sales": total_sales,
        "currency": currency,
        "items": items
    }

    return data

# Function to produce Avro messages to Confluent Cloud
def produce_avro_messages(bootstrap_servers, topic):
    producer_conf = {
        "bootstrap.servers": bootstrap_servers,
        "schema.registry.url": "https://<CONFLUENT_CLOUD_SCHEMA_REGISTRY_URL>",  # Replace with your Confluent Cloud Schema Registry URL
        "sasl.mechanisms": "PLAIN",
        "security.protocol": "SASL_SSL",
        "sasl.username": "<CONFLUENT_CLOUD_API_KEY>",
        "sasl.password": "<CONFLUENT_CLOUD_API_SECRET>"
    }

    producer = Producer(producer_conf)

    while True:
        data = generate_mock_data()
        key = {"id_key": data["id"]}

        # Serialize data to Avro
        value = fastavro.schemaless_writer(data, avro_schema)

        # Send the message to the topic
        producer.produce(topic=topic, value=value, key=key)

        # Wait a little before sending the next message
        time.sleep(1)

if __name__ == "__main__":
    # Replace with your Confluent Cloud bootstrap servers and topic name
    bootstrap_servers = "<CONFLUENT_CLOUD_BOOTSTRAP_SERVERS>"
    topic = "<CONFLUENT_CLOUD_TOPIC_NAME>"
    produce_avro_messages(bootstrap_servers, topic)