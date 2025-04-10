import time

countdown_start = int(input("Enter the time for countdown in seconds: "))

for i in range(countdown_start, 0, -1):
    print(i)
    time.sleep(1)  # Wait for 1 second after each number

print("Time's up!")
