# Kafka_DWH

To run this demo use `docker-compose up`

## What will happen?

-   First the container for Kafka and Zookeeper will be created
-   After 30 seconds the Producer container will be started and will produce 20 messages to the 'Test' topic
-   10 seconds later the Consumer container will be started and print the the messages from the 'Test' topic to the console

## Troubleshooting

If there are issues with the Consumer and Producer images you can build your own in the Consumer and Producer folder. After you have done that you can replace the image in the **docker-compose-yml** file.
