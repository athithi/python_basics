tasks=[]
while True:
    task=input("Enter task or quit: ")
    if task=='quit':
        break
    tasks.append(task)
    print("to do list:", tasks)
