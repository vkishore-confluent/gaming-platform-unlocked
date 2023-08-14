from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

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
    'bootstrap.servers': 'YOUR_BROKER_ENDPOINT',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': 'YOUR_API_KEY',
    'sasl.password': 'YOUR_API_SECRET',
    'schema.registry.url': 'https://CONFLUENT_CLOUD_SCHEMA_REGISTRY_URL'
}

# Create Avro producers
producer = AvroProducer(conf, default_value_schema=purchase_schema, value_schema_registry=conf['schema.registry.url'])
pageview_producer = AvroProducer(conf, default_value_schema=pageview_schema, value_schema_registry=conf['schema.registry.url'])

# Produce events
purchase_event = {
    "item": "example_item",
    "amount": 100.0,
    "customer_id": "customer123"
}

pageview_event = {
    "url": "https://example.com/page",
    "is_special": False,
    "customer_id": "customer456"
}

# Produce Purchase event
producer.produce(topic='your-topic-name', value=purchase_event, value_schema=purchase_schema)

# Produce PageView event
pageview_producer.produce(topic='your-topic-name', value=pageview_event, value_schema=pageview_schema)

# Wait for any outstanding messages to be delivered and delivery reports to be received.
producer.flush()
pageview_producer.flush()

