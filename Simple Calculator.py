print('select the operation')
print(' + => enter 1\n','- => enter 2\n','* => enter 3 \n','/ => enter 4 \n')
num=int(input('enter operation number:'))
int1=int(input('enter integer 1:'))
int2=int(input('enter integer 2:'))
if num==1:
    print('you choosed +')
    total=int1+int2
    print(int1,'+',int2,'=',total)
elif num==2 :   
    print('you choosed -')
    total=int1-int2
    print(int1,'-',int2,'=',total)
elif num==3:
    print('you choosed *')
    total=int1*int2
    print(int1,'*',int2,'=',total)
elif num==4:
    try:
     print('you choosed /')
     total=int1/int2
     print(int1,'/',int2,'=',total)
    except ZeroDivisionError:
        print('Error')
else:
    print('please enter valid option')
