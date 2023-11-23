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
    distance = random.randint(1, 100)
    await asyncio.sleep(2)
    return distance

async def turn():
    '''
    Simulate a turn by waiting for the ultrasonic sensor to return a value less than 50
    '''
    print("Waiting for ultrasonic sensor...")
    distance = await ultrasonic()
    print("Distance: " + str(distance))
    if distance < 50:
        print("Turning...")
        await asyncio.sleep(1)
    else:
        print("Driving forward...")
        await asyncio.sleep(1)

async def main():
    '''
    Simulate a robot by continuously turning and driving forward
    '''
    while True:
        await turn()
        await asyncio.sleep(0.1)

asyncio.run(main())
