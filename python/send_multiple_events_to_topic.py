import time
import random
from confluent_kafka import Producer

# Avro schemas
purchase_schema = {
    "type": "record",
    "namespace": "io.confluent.developer.avro",
    "name": "Purchase",
    "fields": [
        {"name": "item", "type": "string"},
        {"name": "amount", "type": "double"},
        {"name": "customer_id", "type": "string"}
    ]
}

pageview_schema = {
    "type": "record",
    "namespace": "io.confluent.developer.avro",
    "name": "PageView",
    "fields": [
        {"name": "url", "type": "string"},
        {"name": "is_special", "type": "boolean"},
        {"name": "customer_id", "type": "string"}
    ]
}

# Confluent Cloud configuration
conf = {
    'bootstrap.servers': 'pkc-ymrq7.us-east-2.aws.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': 'ZEETRLZDMS5MNMCD',
    'sasl.password': 'FRtUOomJB0Xh6yShIhwr/+TGvVhOi9lgK2mbWzxIbZc6DCdQ1rrwpo/XdPJv6FYQ',
    'schema.registry.url': 'https://psrc-e0919.us-east-2.aws.confluent.cloud'
}

# Create Avro producers
producer = Producer(conf, default_value_schema=purchase_schema)
pageview_producer = Producer(conf, default_value_schema=pageview_schema)

# Continuously produce random events
while True:
    # Generate random Purchase event
    purchase_event = {
        "item": f"item_{random.randint(1, 10)}",
        "amount": round(random.uniform(10.0, 100.0), 2),
        "customer_id": f"customer_{random.randint(1, 100)}"
    }
    producer.produce(topic='avro-events', value=purchase_event, value_schema=purchase_schema)
    
    # Generate random PageView event
    pageview_event = {
        "url": f"https://example.com/page_{random.randint(1, 10)}",
        "is_special": random.choice([True, False]),
        "customer_id": f"customer_{random.randint(1, 100)}"
    }
    pageview_producer.produce(topic='avro-events', value=pageview_event, value_schema=pageview_schema)
    
    # Flush the producers periodically
    if random.random() < 0.1:  # Flush with a probability of 10%
        producer.flush()
        pageview_producer.flush()
    
    # Introduce a small delay before generating the next events
    time.sleep(random.uniform(0.5, 2.0))
