def static_stack():
    stack_object = ["HP", "DELL", "ACER", "LENOVO", "APPLE", "SAMSUNG", "HISENSE"]

    print("List of items in stack are; ")
    for i in range(len(stack_object)):
        print(stack_object[i])

    print("\nList of order of execution for the LAST IN FIRST OUT ALGORITHM will be; ")
    for i in range(len(stack_object)):
        i+=1
        stack_order = stack_object[-i]
        print(stack_order)

    #stack_remaining = stack_order.remove(i)-stack_object[i]
    #stack_remaining = stack_object[-1]
    print("\nItem ", stack_object[-1], " will be out of the stack first.")

    stack_object.remove(stack_object[-1]) 
    #print(stack_object)
    print("Items ramining are: \n")
    for i in range(len(stack_object)):
        i+=1
        #print(stack_object[i])
        print(f" {stack_object[-i]}")


    print("\nItem ", stack_object[5], " will be out of the stack next.")
    if "SAMSUNG" in stack_object:
        print(f" {stack_object}") 

    stack_object.remove(stack_object[5]) 
    
    print("Items ramining are: ")
    for i in range(len(stack_object)):
        i+=1
        #print(stack_object[i])
        print(f" {stack_object[-i]}")

    #get the item to be out of the stack next
    print("\nItem ", stack_object[4], " will be out of the stack next.")

    stack_object.remove(stack_object[4]) 
    
    print("Items ramining are: ")
    for i in range(len(stack_object)):
        i+=1
        #print(stack_object[i])
        print(f" {stack_object[-i]}")

    #get the item to be out of the stack next
    print("\nItem ", stack_object[3], " will be out of the stack next.")

    stack_object.remove(stack_object[3]) 
    
    print("Items ramining are: ")
    for i in range(len(stack_object)):
        i+=1
        #print(stack_object[i])
        print(f" {stack_object[-i]}")


    #get the item to be out of the stack next
    print("\nItem ", stack_object[2], " will be out of the stack next.")

    stack_object.remove(stack_object[2]) 
    
    print("Items ramining are: ")
    for i in range(len(stack_object)):
        i+=1
        #print(stack_object[i])
        print(f" {stack_object[-i]}")

    
    #get the item to be out of the stack next
    print("\nItem ", stack_object[1], " will be out of the stack next.")

    stack_object.remove(stack_object[1]) 
    
    print("Items ramining are: ")
    for i in range(len(stack_object)):
        i+=1
        #print(stack_object[i])
        print(f" {stack_object[-i]}")

    
    #get the item to be out of the stack next
    print("\nItem ", stack_object[0], " will be out of the stack next.")

    stack_object.remove(stack_object[0])
    try:
        if stack_object == []:
            print(f"Stack emptied. Execution terminated")
    except:
        print("Cannot be executed completely.")
    
  


if __name__ == "__main__":
    static_stack()