#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

messages = ["1 Sunday", "2 Monday", "3 Tuesday", "4 Wednesday", "5 Thursday", "6 Friday"];

for message in messages:
	channel.basic_publish(exchange='',
						  routing_key='hello',
						  body=message)
	print(" [x] Send Message '" + message + "'")
	time.sleep(1)

connection.close()