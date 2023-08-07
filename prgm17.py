#stack operation

stack = []
def push(element):
    stack.append(element)
    print("element ", element , "pushed onto a the stack")

def pop():
    if len(stack) == 0:
        print("stack is empty.cannot perform stack operation")
    else:
        element = stack.pop()
        print("element ", element , "popped onto a the stack")

def  display():
    if len(stack) == 0:
        print("stack is empty")
    else:
        print("element in stack: ",stack)
    

while True:
    print("stack operations:")
    print("1.push")
    print("2.pop")
    print("3.display")
    print("4.quit")

    choice = int(input("enter yours choice (1-4):"))

    if choice == 1:
        element = (input("enter element to be push:"))
        push(element)

    elif choice == 2:
        pop()
    elif display()==3:
        display()
    elif choice == 4:
        break
    else:
        print("invalid choice")
        

