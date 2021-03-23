from kafka import KafkaConsumer
from json import loads
import logging
import time
from sys import argv
#logging.basicConfig(level=logging.DEBUG)

def consume():
   print('\n<Consuming>')
   consumer = KafkaConsumer(
      'Test',
      auto_offset_reset='earliest',
      enable_auto_commit=True,
      group_id=None,
      #value_deserializer=lambda m: loads(m.decode('utf-8')),
      bootstrap_servers=[bootstrap_server])


   for m in consumer:
      print(m.value)

try:
    bs=argv[1]
    print('\n🥾 bootstrap server: {}'.format(bs))
    bootstrap_server=bs
except:
    # no bs X-D
    bootstrap_server='localhost:19092'
    print('⚠️  No bootstrap server defined, defaulting to {}\n'.format(bootstrap_server))

try:
      consume()

except Exception as e:
        print("❌ (uncaught exception in consume): ", e)