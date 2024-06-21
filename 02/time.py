
l = list(map(int, input().split()))
i = 0
boo = True
while True:
    try:
        l[i]
        try:
            l[i+1]
        except:
            print("Odd")
            break
    except:
        print("Even")
        boo = False
        break
    i += 2
