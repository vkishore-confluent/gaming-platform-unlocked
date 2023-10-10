from uuid import uuid4
import os, random
from confluent_kafka.schema_registry import SchemaRegistryClient

import argparse
from confluent_kafka import Consumer
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry.avro import AvroDeserializer

# update your cluster credentials here
cluster_bootstrap = 'pkc-l7pr2.ap-south-1.aws.confluent.cloud:9092'
cluster_api_key = 'ANEXNLPCC3VKDOIC'
cluster_api_secret = 'LcZvNW/vk3XgOYjqjZMvEI3BWkkw6yeoq7xoGmX3VSqgQ2qYinhJwW7bsm3LjxOI'

# update your schema registry credentials here
schemaregistry_url = 'https://psrc-4r3xk.us-east-2.aws.confluent.cloud'
schemaregistry_api_key = '6BAXBHCKOZBKULLP'
schemaregistry_api_secret = 'MsX2pdup+eBArSHsTowAyFf4SIGDRhyQcKrDH9ak13aF64GhOsGPfP96Xfg4Sc/E'


class PlayerHealth(object):
    def __init__(self, player_id=None, health=None, timestamp=None):
        self.player_id = player_id
        self.health = health
        self.timestamp = timestamp

def dict_to_player_health(obj, ctx):
    if obj is None:
        return None
    return PlayerHealth(player_id=obj['player_id'],
                health=obj['health'],
                timestamp=obj['timestamp'])

# class PlayerPosition(object):
#     def __init__(self, player_id, x, y):
#         self.player_id = player_id
#         self.x = x
#         self.y = y

# def player_position_to_dict(player_health, ctx):
#     return dict(player_id=player_health.player_id,
#                 x=player_health.x,
#                 y=player_health.y)

def delivery_report(err, msg):
    if err is not None:
        print("Delivery failed for User record {}: {}".format(msg.key(), err))
        return
    else:
        print('User record {} successfully produced to {} [{}] at offset {}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))

def main():
    topic = 'game-events'
    schema0 = 'player_health.avsc'
    # schema1 = 'player_position.avsc'
    path = os.path.realpath(os.path.dirname(__file__))[:-6] + 'terraform/schemas/'
    with open(f"{path}{schema0}") as f0:
        schema_str0 = f0.read()
    # with open(f"{path}{schema1}") as f1:
    #     schema_str1 = f1.read()

    schema_registry_conf = {
        'url': schemaregistry_url,
        'basic.auth.user.info': schemaregistry_api_key + ':' + schemaregistry_api_secret
        }
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)
    
    serializer_configs = {
        'auto.register.schemas': False,
        'use.latest.version': True
    }

    avro_deserializer = AvroDeserializer(schema_registry_client,
                                         schema_str0,
                                         dict_to_player_health)
    # string_serializer = StringSerializer('utf_8')
    # avro_serializer0 = AvroSerializer(schema_registry_client,schema_str0,player_health_to_dict, serializer_configs)
    # avro_serializer1 = AvroSerializer(schema_registry_client,schema_str1,player_position_to_dict, serializer_configs)

    consumer_conf = {'bootstrap.servers': cluster_bootstrap,
                     'group.id': 'producer_py',
                     'auto.offset.reset': 'earliest',
                     'security.protocol': 'SASL_SSL',
                     'sasl.mechanism': 'PLAIN',
                     'sasl.username': cluster_api_key,
                     'sasl.password': cluster_api_secret}

    consumer = Consumer(consumer_conf)
    consumer.subscribe([topic])

    # producer_conf = {
    #     'bootstrap.servers': cluster_bootstrap,
    #     'client.id': 'producer_py',
    #     'security.protocol': 'SASL_SSL',
    #     'sasl.mechanism': 'PLAIN',
    #     'sasl.username': cluster_api_key,
    #     'sasl.password': cluster_api_secret,
    #     'linger.ms': 0,
    #     'batch.size': 65536,
    #     'request.timeout.ms': 900000,
    #     'queue.buffering.max.ms': 100,
    #     'retries': 10000000,
    #     'socket.timeout.ms': 500,
    #     'default.topic.config': {
    #         'acks': 'all',
    #         'message.timeout.ms': 5000,
    #         }
    #     }
    # producer = Producer(producer_conf)

    while True:
        try:
            # SIGINT can't be handled when polling, limit timeout to 1 second.
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            user = avro_deserializer(msg.value(), SerializationContext(msg.topic(), MessageField.VALUE))
            if user is not None:
                print("User record {}: player_id: {}\n"
                      "\health: {}\n"
                      "\timestamp: {}\n"
                      .format(msg.key(), user.player_id,
                              user.health,
                              user.timestamp))
        except KeyboardInterrupt:
            break
        except TypeError:
            continue

    consumer.close()

    # print("Producing record to topic {}. ^C to exit.".format(topic))
    # while True:
        # choice = random.randint(0, 1)
        # producer.poll(0.0)
        # if choice == 0:
        #     print('Generating [PlayerHealth] record.')
        #     player_id = gen_player_id()
        #     health = gen_health()
        #     timestamp = 1660857600000
        #     try: 
        #         playerhealth = PlayerHealth(player_id=player_id,
        #                     health=health,
        #                     timestamp=timestamp)
        #         producer.produce(topic=topic,
        #                             key=string_serializer(str(uuid4())),
        #                             value=avro_serializer0(playerhealth, SerializationContext(topic, MessageField.VALUE)),
        #                             on_delivery=delivery_report)
        #     except ValueError:
        #         print("Invalid input, discarding record...")
        # elif choice == 1:
        #     print('Generating [PlayerPosition] record.')
        #     player_id = gen_player_id()
        #     x = gen_x()
        #     y = gen_y()
        #     try: 
        #         playerposition = PlayerPosition(player_id=player_id,
        #                     x=x,
        #                     y=y)
        #         print(avro_serializer1(playerposition, SerializationContext(topic, MessageField.VALUE)))
        #         producer.produce(topic=topic,
        #                             key=string_serializer(str(uuid4())),
        #                             value=avro_serializer1(playerposition, SerializationContext(topic, MessageField.VALUE)),
        #                             on_delivery=delivery_report)
        #     except ValueError:
        #         print("Invalid input, discarding record...")
        
        #print("\nFlushing records...")
        # producer.flush()

def gen_player_id():
    return 'player' + str(random.randint(1, 15))

def gen_health():
    return int(random.randint(10, 99))

def gen_x():
    return float(random.randint(101,999)/10)

def gen_y():
    return float(random.randint(101,999)/10)

if __name__ == '__main__':
    main()