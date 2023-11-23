'''
This program demonstrates how to use the asyncio library to simulate
a robot turning based on an ultrasonic sensors reading.
'''

import asyncio
import random

async def ultrasonic():
    '''
    Simulate an ultrasonic sensor by returning a random number between 1 and 100 every 2 seconds
    '''
    while True:
        global distance
        distance = random.randint(1, 100)
        await asyncio.sleep(2)

async def turn():
    '''
    Simulate a turn by waiting for the ultrasonic sensor to return a value less than 50
    '''
    while True:
        print("Waiting for ultrasonic sensor...")
    # distance = await ultrasonic()
        print("Distance: " + str(distance))
        if distance < 50:
            print("Turning...")
            await asyncio.sleep(1)
        else:
            print("Driving forward...")
            await asyncio.sleep(1)

event_loop = asyncio.get_event_loop()
event_loop.create_task(ultrasonic())
event_loop.create_task(turn())
event_loop.run_forever()
