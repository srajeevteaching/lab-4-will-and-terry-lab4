# Programmers: [your names]
# Course: CS151,
# Dr. Rajeev Date: Thu Oct 7
# Lab: 4
# Program Inputs: [DataPlan, GB of data]
# Program Outputs: [the amount they owe their data provider]# lab4fall
plan=(input("please input the name of your plan").lower()).replace(" ","")
gb=float(input("in gigabytes how much data have you used"))

cost=0
if plan=="green":
    coupon=(input("do you have a coupon? Yes or No").lower()).replace(" ","")
    if coupon=="yes":
        if gb <=2:
            cost=49.99
        else:
            cost=49.99+14.99*(gb-2)
        if cost>=75:
            cost-=20
    else:
        if gb <= 2:
            cost = 49.99
        else:
            cost = 49.99 + 14.99 * (gb - 2)
elif plan=="orange":
    if gb <= 4:
        cost = 69.99
    else:
        cost = 69.99 + 9.99 * (gb - 4)
elif plan=="purple":
    cost=99.99
print("your cost is $%.2f" %cost)