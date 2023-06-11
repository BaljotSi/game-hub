import time

limit = int(input("Enter Seconds for timer: "))

for i in range(limit):
    print("Time " , i)
    time.sleep(1)

start = time.time()


time.sleep(1)
print(" Time is over")



