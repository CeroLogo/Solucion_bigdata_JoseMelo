from kafka import KafkaProducer
import json
import time
import random

# Configura el productor
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Simula datos aleatorios y envíalos a Kafka
def send_data():
    while True:
        data = {
            "event_id": random.randint(1, 100),
            "value": random.uniform(10.0, 100.0),
            "timestamp": time.time()
        }
        producer.send('real_time_topic', data)
        print(f"Sent: {data}")
        time.sleep(1)  # Controla la frecuencia de envío

if __name__ == "__main__":
    send_data()
