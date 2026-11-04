gender=input("Enter Gender (male/female):")
hb=float(input("enter hemoglobin level:"))
if gender=="female":
    if hb<117:
        print("hemoglobin is low.")
    elif hb<=155:
        print("hemoglobin is normal.")
    else:
        print("hemoglobin is high.")
elif gender=="male":
    if hb<134:
        print("hemoglobin is low.")
    elif hb<=167:
        print("hemoglobin is normal.")
    else:
        print("hemoglobin is high.")
else:
    print("invalid gender")
