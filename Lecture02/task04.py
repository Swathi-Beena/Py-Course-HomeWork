year=int(input("enter year:"))
if year / 400 == year//400:
    print("leap year")
elif year / 100 == year // 400:
    print("not leap year")
elif year / 4 == year//4:
    print("leap year")
else:
    print("not leap year")