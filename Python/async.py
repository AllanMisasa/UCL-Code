import asyncio
import random

async def ultrasonic():
    # Random integer between 1 and 100
    distance = random.randint(1, 100)
    await asyncio.sleep(2)
    return distance
    
async def turn():
    print("Waiting for ultrasonic sensor...")
    distance = await ultrasonic()
    print("Distance: " + str(distance))
    if distance < 50:
        print("Turning...")
    else:
        print("Driving forward...")
    
async def main():
    while True:
        await turn()
        await asyncio.sleep(0.1)

asyncio.run(main())