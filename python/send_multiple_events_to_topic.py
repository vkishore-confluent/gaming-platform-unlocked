from uuid import uuid4

from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer

schemaregistry_url = 'https://psrc-l7y22.us-east-2.aws.confluent.cloud'
schemaregistry_auth = 'BJKQ6LZWEFW3OGIT:CYqjlVhoOd+KgIpFxH5I5dlS5d4MsUViMaF1p4k53k9Y4vr/jePZF1Nic/QndmGc'

class PlayerHealth(object):
    def __init__(self, player_id, health, timestamp):
        self.player_id = player_id
        self.health = health
        self.timestamp = timestamp


def player_health_to_dict(player_health, ctx):
    return dict(player_id=player_health.player_id,
                health=player_health.health,
                timestamp=player_health.timestamp)


def delivery_report(err, msg):
    if err is not None:
        print("Delivery failed for User record {}: {}".format(msg.key(), err))
        return
    print('User record {} successfully produced to {} [{}] at offset {}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))


def main():
    topic = 'game-events'
    with open('/Users/vkishore/Desktop/gaming-platform-unlocked/terraform/schemas/player_health.avsc') as f:
        schema_str = f.read()
    schema_str = """{
        "type": "record",
        "namespace": "io.confluent.developer.avro",
        "name": "PlayerHealth",
        "fields": [
            {
                "name": "player_id",
                "type": "string"
            },
            {
                "name": "health",
                "type": "int"
            },
            {
                "name": "timestamp",
                "type": "long"
            }
        ]
    }"""

    schema_registry_conf = {
        'url': schemaregistry_url,
        'basic.auth.user.info': schemaregistry_auth
        }
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)

    avro_serializer = AvroSerializer(schema_registry_client,schema_str,player_health_to_dict)

    string_serializer = StringSerializer('utf_8')

    producer_conf = {
        'bootstrap.servers': 'https://pkc-921jm.us-east-2.aws.confluent.cloud:9092',
        'client.id': 'producer_py',
        'security.protocol': 'SASL_SSL',
        'sasl.mechanism': 'PLAIN',
        'sasl.username': 'P7YABYMXUIBEFIYH',
        'sasl.password': 'Mo8jWtUBPHqzg/lWbLj2k54xPulLy8m09SX2FWowcGm355jTNqiKEbDP8/Q1A44c'
        }

    producer = Producer(producer_conf)

    print("Producing record to topic {}. ^C to exit.".format(topic))
    while True:
        # Serve on_delivery callbacks from previous calls to produce()
        producer.poll(0.0)
        try:
            player_id = 'player123'
            health = 96
            timestamp = 1660857600000
            playerhealth = PlayerHealth(player_id=player_id,
                        health=health,
                        timestamp=timestamp)
            print(avro_serializer(playerhealth, SerializationContext(topic, MessageField.VALUE)))
            producer.produce(topic=topic,
                             key=string_serializer(str(uuid4())),
                             value=avro_serializer(playerhealth, SerializationContext(topic, MessageField.VALUE)),
                             on_delivery=delivery_report)
        except KeyboardInterrupt:
            break
        except ValueError:
            print("Invalid input, discarding record...")
            continue

    print("\nFlushing records...")
    producer.flush()


if __name__ == '__main__':
    main()