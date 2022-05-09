from time import sleep as slp
i = 0;flag = True;lengvawe = 1;j=0
def operation(fla):
    global i
    i=i+1 if fla else i-1
while True:
    print(" "*j," "*i,"Global Warming")
    operation(flag)
    if lengvawe%7==0:
        flag = not flag
    if lengvawe%14==0:
        j=j+1
    lengvawe +=1
    slp(0.23)