num1=int(input('enter the cost of the meal:'))
print('satisfaction level\n','1=totally satisfied\n','2=satisfied\n','3=dissatisfied\n')
num2=int(input('enter satisfaction level:'))
print('satisfaction level:',num2)

if num2==1:
        tip=num1*0.2
elif num2==2:
        tip=num2*0.15
elif num2==3:
        tip=num2*0.10
else:
 print('please enter valid number')
try:
 print('tip:',tip)
except NameError:
    print('please enter valid satisfaction level.then I will calculate the tip')
