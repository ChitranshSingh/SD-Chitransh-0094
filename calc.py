def add(a, b):
    print('Addition =',a+b)
def sub(a, b):
    print('Subtraction =',a-b)
def mul(a, b):
    print('Multiplication =',a*b)
def div(a, b):
    print('Division =',a/b)

def menu():
    print('\n----------Calculator----------')

    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    print('\n\nOperations\n1. Add\n2. Sub\n3. Multiplication\n4. Division')


    ch = int(input("\n\nEnter Choice(1-4): "))

    if(ch==1):
        add(a,b)
    elif(ch==2):
        sub(a,b)
    elif(ch==3):
        mul(a,b)
    elif(ch==4):
        div(a,b)
    else:
        print('\n worng operation')


menu()