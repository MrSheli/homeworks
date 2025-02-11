# მომხმარებელს შემოატანინე ისევ 5 განსხვავებული რიცხვი, შემდეგ კი დაპრინტე: ყველაზე მცირე რიცხვი, ყველაზე დიდი რიცხვი, ელემენტების რაოდენობა, რიცხვების ჯამი და ბოლოს არითმეტიკული საშვალო ამ რიცხვების 

num = int(input("enter number: "))
num0 = int(input("enter number: "))
num1 = int(input("enter number: "))
num2 = int(input("enter number: "))
num3 = int(input("enter number: "))




print(min(num,num0,num1,num2,num3))

print(max(num,num0,num1,num2,num3))

print(len([num,num0,num1,num2,num3]))

print(sum([num,num0,num1,num2,num3]))

print([sum([num,num0,num1,num2,num3]) / len([num,num0,num1,num2,num3])])
