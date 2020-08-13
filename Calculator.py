def Calc(OpInput,Num1,Num2):
    total = 0
    if OpInput == '+':
        total = int(Num1) + int(Num2)
        return total
        print(total)
    elif OpInput == '-':
        total = int(Num1) - int(Num2)
        return total
        print(total)
    elif OpInput == 'x':
        total = int(Num1) * int(Num2)
        return total
        print(total)
    elif OpInput == '/':
        total = int(Num1) / int(Num2)
        return total
        print(total)
    else:
        print("Invalid Operator entered")
G_total = 0
with open("C:\\Users\\P10304269\\OneDrive - Capita\\Documents\\DevOpsStep2.txt",'r') as f:
    text_string = f.read().splitlines()
    for line in text_string:
        start, OpInput, Num1, Num2 = line.split()
        Total = Calc(OpInput, Num1, Num2)
        G_total = G_total + Total
        print(G_total)



