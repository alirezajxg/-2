# دریافت چهار عدد از کاربر
num1 = float(input("عدد اول را وارد کنید: "))
num2 = float(input("عدد دوم را وارد کنید: "))
num3 = float(input("عدد سوم را وارد کنید: "))
num4 = float(input("عدد چهارم را وارد کنید: "))

# پیدا کردن بزرگترین عدد با استفاده از if و else
if num1 >= num2 and num1 >= num3 and num1 >= num4:
     print("num1")
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    print("num2")
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    print("num3")
else:
    print("num4")

# نمایش نتیجه
print(f"بزرگترین عدد: {largest}")


