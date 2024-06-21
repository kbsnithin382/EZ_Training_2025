# seconds to time

n = int(input())

hours = n // 3600
n %= 3600
minutes = n // 60
n %= 60
seconds = n

print(f"{hours}h : {minutes}m : {seconds}s")