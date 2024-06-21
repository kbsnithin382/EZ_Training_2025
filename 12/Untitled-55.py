
days = int(input())

years = days // 360
days %= 360

months = days // 30
days %= 30

weeks = days // 6

days %= 6

print(f"{years}y {months}m {weeks}w {days}d")

