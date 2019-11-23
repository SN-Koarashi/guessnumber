# Python 3
import random
ans = random.randint(1,100)
for i in range(1,4):
    q = int(input("Type number: "))
    if q == ans:
        print("SUCCESS!",ans)
        break
    elif i == 3:
        print("FAILD, Correct answer",ans)
    else:
        higher = ans+random.randint(1,10)
        lower = ans-random.randint(1,10)
        if q > ans:
            print("Too hight, range",str(lower)+"~"+str(q))
        elif q < ans:
            print("Too lower, range",str(q)+"~"+str(higher))
        continue
