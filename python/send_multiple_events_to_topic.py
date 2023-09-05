from uuid import uuid4
import os
from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer

# update your cluster credentials here
cluster_bootstrap = 'https://pkc-921jm.us-east-2.aws.confluent.cloud:9092'
cluster_api_key = 'IGNB3OO4JDOCVKTL'
cluster_api_secret = 'e+o1i6Abo/zr6s19XiK3a2Sbkm0uZYLow1PcDEBENDqhadfHU1qpoooSbx+NXcqi'

# update your schema registry credentials here
schemaregistry_url = 'https://psrc-mw731.us-east-2.aws.confluent.cloud'
schemaregistry_api_key = 'FIR4XN4O4YUFULIW'
schemaregistry_api_secret = 'ywNpZ/UjltSxLyYSe6vKRLYmsZHXicvv71T5+TCQeMck96ZHqS+L0S1hRIeuAeGZ'

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

    schema = 'player_health.avsc'
    path = os.path.realpath(os.path.dirname(__file__))[:-6] + 'terraform/schemas/'
    with open(f"{path}{schema}") as f:
        schema_str = f.read()

    schema_registry_conf = {
        'url': schemaregistry_url,
        'basic.auth.user.info': schemaregistry_api_key + ':' + schemaregistry_api_secret
        }
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)

    avro_serializer = AvroSerializer(schema_registry_client,schema_str,player_health_to_dict)
    string_serializer = StringSerializer('utf_8')
    producer_conf = {
        'bootstrap.servers': cluster_bootstrap,
        'client.id': 'producer_py',
        'security.protocol': 'SASL_SSL',
        'sasl.mechanism': 'PLAIN',
        'sasl.username': cluster_api_key,
        'sasl.password': cluster_api_secret,
        'auto.register.schemas': False,
        'use.latest.version': True
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