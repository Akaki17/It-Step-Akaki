import asyncio
import time
import random


###   1


# async def smoke():
#     print(f'I Started Smoke')
#     await asyncio.sleep(2)
#     print(f'I Finished Smoke')
    
# async def eat_apple():
#     print(f'I Started eat Apple')
#     await asyncio.sleep(5)
#     print(f'I Finished eat Apple')
    
    
# async def main():
    
#     start_time = time.time()
    
#     smoke1 = asyncio.create_task(smoke())
#     eat1 = asyncio.create_task(eat_apple())
    
#     await smoke1
#     await eat1
    
#     end_time = time.time()
#     elapsed_time = end_time - start_time
    
#     print(f'elapsed time: {elapsed_time:.2f} second')

# if __name__ == '__main__':
#     asyncio.run(main())
    


###   2

# async def random_action(number, delay):
#     print(f'Started: {number}')
#     await asyncio.sleep(delay)
#     print(f'Delay {delay:.2f} second')
#     print(f'Finished: {number}')

# async def main():
#     start_time = time.time()
#     tasks = []
#     for number in range(1, 11):
#         delay  = random.randint(1,15)
#         tasks.append(random_action(number, delay))
        
#     await asyncio.gather(*tasks)
    
#     end_time = time.time()
#     elapsed_time = end_time - start_time
    
#     print(f'Elapsed time: {elapsed_time:.2f} second')

# if __name__ == '__main__':
#     asyncio.run(main())
    
    
    
###   3

async def square(number):
    print (f'Square of: {number}: {number ** 2}')

async def check_number(num):
    if num % 2 == 0:
        await square(num)
    else:
        print(f'Number is Odd. Try to Even.')
        
async def main():
    
    user_input = int(input('"Enter Number: '))
    
    await asyncio.gather(
            check_number(user_input)
            
            # square(user_input) if user_input % 2 == 0 else asyncio.sleep(0)
    )
    


if __name__ == '__main__':
    asyncio.run(main())