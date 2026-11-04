length=float(input("Enter the length of zender in cm:"))
if length<42:
    short=42-length
    print(f"Release the fish back into the lake. It is {short} cm short of the limit.")
else:
    print("You can keep the fish.")
