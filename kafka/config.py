import asyncio

# env Variable
KAFKA_BOOTSTRAP_SERVERS= "localhost:9092"
KAFKA_TOPIC="demo-topic"
KAFKA_CONSUMER_GROUP="group-id"
loop = asyncio.get_event_loop()
