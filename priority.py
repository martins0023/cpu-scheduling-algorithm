#PRIORITY TEST
#create a function for the priority scheduling
def priority_scheduling():
    #create a list for the processes, priorities, execution time, and burst time
    process = ["HOTDOG", "CORN", "BACON", "CHEESE"]
    exec_time = [5, 6, 2, 8]
    priority = [2, 9, 4, 8]
    burst_time = [4, 3, 8, 6]

    #loop over the range off all executions and get the summation
    for i in range(len(exec_time)):
        summation_of_all_exec = sum(exec_time)


    #loop through the processes and their corresponding values and print them in a tabular format
    print(f"PROCESS NAME \t EXECUTION TIME \t PRIORITY \t BURST TIME")
    for i in range(len(process)):
        print(f'{process[i]} \t\t {exec_time[i]} \t\t\t {priority[i]} \t\t {burst_time[i]}')
    
    max_priority = max(priority) #get the maximum priority
    print(f"\nThe maximum priority for the process is {max_priority}") #print out the maximum priority

    process_index = process[priority.index(max_priority)] #GET THE PROCESS INDEX FOR THE CORRESPONDING HIGHEST PRIORITY NUMBER
    execution_time_index = exec_time[priority.index(max_priority)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING HIGHEST PRIORITY NUMBER
    burst_time_index = burst_time[priority.index(max_priority)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING HIGHEST PRIORITY NUMBER

    if priority.index(max_priority) == priority.index(max_priority):
        print(f" \nSo therefore process {process[priority.index(max_priority)]} will be out of the stack first and will be executed for 0 - {exec_time[priority.index(max_priority)]} time length.")

    #calculate the time length for each execution
    sum_time_length = exec_time[priority.index(max_priority)]

    #REMOVE ALL CORRRESPONDING INDEX TO THE MAXIMUM PRIORITY GOTTEN
    process.remove(process_index)
    exec_time.remove(execution_time_index)
    priority.remove(priority[priority.index(max_priority)])
    burst_time.remove(burst_time_index)

    print("______________________________________________________________________________\nprocesses left with their corresponding busrt, execution time and priority; ")
    print(f"\nPROCESS NAME \t EXECUTION TIME \t PRIORITY \t BURST TIME")
    for i in range(len(priority and process)):
        
        #print(stack_object[i])
        print(f'\n{process[i]} \t\t {exec_time[i]} \t\t\t {priority[i]} \t\t {burst_time[i]}')
        next_priority = max(priority)

    print(f"\nThe next maximum priority for the process is {next_priority}")

    process_index = process[priority.index(next_priority)] #GET THE PROCESS INDEX FOR THE CORRESPONDING HIGHEST PRIORITY NUMBER
    execution_time_index = exec_time[priority.index(next_priority)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING HIGHEST PRIORITY NUMBER
    burst_time_index = burst_time[priority.index(next_priority)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING HIGHEST PRIORITY NUMBER

    #get and calculate the next summation for execution time
    summation_time_length = sum_time_length+exec_time[priority.index(next_priority)]
    if priority.index(next_priority) == priority.index(next_priority):
        print(f" \nSo therefore process {process[priority.index(next_priority)]} will be out of the stack next and will be executed for {sum_time_length} - {summation_time_length} time length.")

    process.remove(process_index)
    exec_time.remove(execution_time_index)
    priority.remove(priority[priority.index(next_priority)])
    burst_time.remove(burst_time_index)

    print("______________________________________________________________________________\nprocesses left with their corresponding busrt, execution time and priority; ")
    print(f"\nPROCESS NAME \t EXECUTION TIME \t PRIORITY \t BURST TIME")
    for i in range(len(priority and process)):
        
        #print(stack_object[i])
        print(f'\n{process[i]} \t\t {exec_time[i]} \t\t\t {priority[i]} \t\t {burst_time[i]}')
        next_priority = max(priority)

    print(f"\nThe next maximum priority for the process is {next_priority}")

    process_index = process[priority.index(next_priority)] #GET THE PROCESS INDEX FOR THE CORRESPONDING HIGHEST PRIORITY NUMBER
    execution_time_index = exec_time[priority.index(next_priority)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING HIGHEST PRIORITY NUMBER
    burst_time_index = burst_time[priority.index(next_priority)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING HIGHEST PRIORITY NUMBER

    #get and calculate the next summation for execution time
    next_summation = summation_time_length+exec_time[priority.index(next_priority)]

    if priority.index(next_priority) == priority.index(next_priority):
        print(f" \nSo therefore process {process[priority.index(next_priority)]} will be out of the stack next and will be executed for {summation_time_length} - {next_summation} time length.")

    process.remove(process_index)
    exec_time.remove(execution_time_index)
    priority.remove(priority[priority.index(next_priority)])
    burst_time.remove(burst_time_index)

    print("______________________________________________________________________________\nprocesses left with their corresponding busrt, execution time and priority; ")
    print(f"\nPROCESS NAME \t EXECUTION TIME \t PRIORITY \t BURST TIME")
    #get the range of remaining processes, priority, execution time, and burst time and print them in a tabular format
    for i in range(len(priority and process)):
        
        print(f'\n{process[i]} \t\t {exec_time[i]} \t\t\t {priority[i]} \t\t {burst_time[i]}')
        next_priority = max(priority)

    print(f"\nThe next maximum priority for the process is {next_priority}")

    process_index = process[priority.index(next_priority)] #GET THE PROCESS INDEX FOR THE CORRESPONDING HIGHEST PRIORITY NUMBER
    execution_time_index = exec_time[priority.index(next_priority)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING HIGHEST PRIORITY NUMBER
    burst_time_index = burst_time[priority.index(next_priority)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING HIGHEST PRIORITY NUMBER

    next_summation_obj = next_summation+exec_time[priority.index(next_priority)]

    if priority.index(next_priority) == priority.index(next_priority):
        print(f" \nSo therefore process {process[priority.index(next_priority)]} will be out of the stack next and will be executed for {next_summation} - {next_summation_obj} time length.")

    process.remove(process_index) #remove the corresponding process
    exec_time.remove(execution_time_index) #remove the corresponding execution time from the list
    priority.remove(priority[priority.index(next_priority)]) #remove the corresponding priority from the list
    burst_time.remove(burst_time_index) #remove the corresponding burst time from the list

    if exec_time == []:
        print(f'\nAll execution has been completed successfully! \nTotal number of executions = {summation_of_all_exec}')

#execute the program function
if __name__ == "__main__":
    priority_scheduling()