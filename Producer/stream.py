from kafka import KafkaProducer
from json import dumps
import logging
import time
from sys import argv
#logging.basicConfig(level=logging.DEBUG)
def produce():
   # write to the topic
   print('\n<Producing>')
   producer = KafkaProducer(bootstrap_servers=[bootstrap_server])
   for i in range(20):
      producer.send('Test', ('Message: ' + str(i)).encode() )
   producer.flush()
   producer.close(timeout=2)

try:
    bs=argv[1]
    print('\n🥾 bootstrap server: {}'.format(bs))
    bootstrap_server=bs
except:
    # no bs X-D
    bootstrap_server='localhost:19092'
    print('⚠️  No bootstrap server defined, defaulting to {}\n'.format(bootstrap_server))

try:
      produce()

except Exception as e:
        print("❌ (uncaught exception in produce): ", e)