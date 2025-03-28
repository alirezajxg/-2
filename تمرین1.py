score=int(input("نمره کسب شده:"))
if 90<=score<=100:
    print("نمره عالی ")
elif 70<=score<=90:
    print("نمره خوب")
elif 50<=score<=70:
    print("نمره متوسط")
elif score<50:
    print("مردود")
else:
    print("سن وارد شده نامعتبر")
