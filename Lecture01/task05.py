talents=float(input("Enter talents: "))
pounds=float(input("Enter pounds: "))
lots=float(input("Enter lots: "))
Total_grams=(talents*20*32+pounds*32+lots)*13.3
kg=int(Total_grams//1000)
g=Total_grams %1000
print(f"The weight in modern units: \n {kg} kilogram and \n {g:.2f} grams")
