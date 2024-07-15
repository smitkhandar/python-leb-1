a=float(input("enter your python marks="))
b=float(input("enter your cyber security marks="))
c=float(input("enter your j2EE marks="))
d=float(input("enter your project marks="))
e=float(input("enter your leb asignment marks="))

tot = a + b + c + d + e
print(f"Total marks = " , tot)
avg = tot / 5
print(f"average marks = " , avg)

if avg >= 91 and avg <= 100:
    print("Your Grade is A1")
elif avg >= 81 and avg < 91:
    print("Your Grade is A2")
elif avg >= 71 and avg < 81:
    print("Your Grade is B1")
elif avg >= 61 and avg < 71:
    print("Your Grade is B2")
elif avg >= 51 and avg < 61:
    print("Your Grade is C1")
elif avg >= 41 and avg < 51:
    print("Your Grade is C2")
elif avg >= 33 and avg < 41:
    print("Your Grade is D")
elif avg >= 21 and avg < 33:
    print("Your Grade is E1")
elif avg >= 0 and avg < 21:
    print("Your Grade is E2")
    

