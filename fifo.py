#USING QUEUE OF GIVEN OBJECTS AND DYNAMICALLY ASSIGNED VALUES 
#Index starts at 0
#This program test consists of two functions, one for allocated static values and two for an allocated dynamic value a user can input to the program for execution. The Dynamic function allows a test for First In First Out Algorithm with assigned values
#by user input and the Static function has assigned values that does not require user input
def dynamic_queue():
    #in a dynamic queue, a user is allowed to add items to the queue intentionally to satisfy the condition of items added to a queue.
    def dynamic_execution():
        print("You will be prompted to execute objects on the queue step by step.") 
        for i in range(len(objects_in_created_queue)):
            steps_execution = len(objects_in_created_queue)-1
            input("Enter next to execute the next object: ")
            print("\n object " + objects_in_created_queue[i] + " will be attended to now... ")
        print("\n --------------------compilation succeeded --------------------\n All objects successfully attended to.")


    objects_in_created_queue = []

    no_of_items = int(input("Enter the number of items you  wish to be queued for : "))
    
    #create a for loop over the number of items entered
    for i in range(no_of_items):
        add_objects_to_queue = input("Enter the object to be queued for : ")
        objects_in_created_queue.append(add_objects_to_queue)
        #print(objects_in_created_queue)

    #loop over object that has been added to the queue list
    for i in range(len(objects_in_created_queue)):
        print("Available object on queue "+ str(i) + " is: " + objects_in_created_queue[i])

        print("object on queue " + str(i) + " will be attended to next... then, object " + str(i+1))

    compute_next_object = input("Has the first object on the queue completed it's execution successfully? (y/n): ")
    
    if compute_next_object.upper() == "N":
        print("\n objects remaining on queue still remains : ", len(objects_in_created_queue))

        user_thought = input("Do you wish to execute all actions for objects on queue at once? (y/n): ")    
    
        if user_thought.upper() == "Y":
            for i in range(len(objects_in_created_queue)):
                print("object on queue " + str(i) + " has been successfully executed... object " + str(i+1), " will be executed next..")
            print("All actions for objects on queue have been successfully executed")
        elif user_thought.upper() == "N":
            print("There are no more suggestions for objects on queue to be executed in this program.")
            dynamic_execution()

            #step_by_step_execution
            #print("You will be prompted to execute objects on the queue step by step.") 
            #for i in range(len(objects_in_created_queue)):
            #    steps_execution = len(objects_in_created_queue)-1
            #    input("Enter next to execute the next object: ")
            #    print("\n object " + objects_in_created_queue[i] + " will be attended to now... ")
            #print("\n --------------------compilation succeeded --------------------")

    elif compute_next_object.upper() == "Y":
        object_remaining = len(objects_in_created_queue)-1
        print("\n objects remaining on queue is :", object_remaining)


    
def static_queue():
    #in the static queue, a user is not allowed to add items to the queue. Already created static objects has been given for execution and testing of the Algorithmm of First Come First Serve.
    objects_on_queue = ['cat', 'dog', 'snake', 'lizard', 'lion', 'hen']
    for i in range(len(objects_on_queue)):
        
        print("Available object on queue "+ str(i) + " is: " + objects_on_queue[i])
         
        print("object on queue " + str(i) + " will be attended to next... then, object " + str(i+1))

    
    compute_next_object = input("Has the first object on the queue completed it's execution successfully? (y/n): ")
    
    
    if compute_next_object.upper() == "N":
        print("\n objects remaining on queue still remains : ", len(objects_on_queue))

        user_thought = input("Do you wish to execute all actions for objects on queue at once? (y/n): ")    
    
        if user_thought.upper() == "Y":
            for i in range(len(objects_on_queue)):
                print("object on queue " + str(i) + " has been successfully executed... object " + str(i+1), " will be executed next..")
            print("All actions for objects on queue have been successfully executed")
        elif user_thought.upper() == "N":
            print("There are no more suggestions for objects on queue to be executed in this program.")
            create_new_queue = input("Would you like to create a new queue for new objects to be executed in this Algorithm? (y/n): ")
            if create_new_queue.upper() == "Y":
                dynamic_queue()
            elif create_new_queue.upper() == "N":
                print("No more available executions for objects in this queue to be excuted.")

    elif compute_next_object.upper() == "Y":
        object_remaining = len(objects_on_queue)-1
        print("\n objects remaining on queue is :", object_remaining)

    
if __name__ == "__main__":
    static_queue()
    #dynamic_queue()