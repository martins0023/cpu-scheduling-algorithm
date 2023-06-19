#SHORTEST JOB FIRST
def shortest_job_first():
    #create a list of jobs with their corresponding arrival time, execution time, and service time.
    process = ["CASHEW", "PINEAPPLE", "LOLLIPOP", "JERGENS"]
    arrival_time = [0, 1, 2, 3]
    exec_time = [10, 7, 2, 9]
    service_time = [8, 13, 11, 20]

    #loop over the range of all execution time and get the summation of it all
    for i in range(len(exec_time)):
        summation_of_all_exec = sum(exec_time)


    #print all processes, execution time, service time in a tabular format
    print(f"\nPROCESS NAME \t ARRIVAL TIME \t\t EXECUTION TIME \t SERVICE TIME")
    for i in range(len(process)):
        print(f'\n {process[i]} \t\t {arrival_time[i]} \t\t\t {exec_time[i]} \t\t\t {service_time[i]}')
   
    #get the shortest job first to start computation and execution
    shortest_job = min(service_time)
    print(f"\nThe shortest job first for the process is {shortest_job}")

    process_index = process[service_time.index(shortest_job)] #GET THE PROCESS INDEX FOR THE CORRESPONDING SHORTEST JOB PROCESS NUMBER
    execution_time_index = exec_time[service_time.index(shortest_job)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING SHORTEST JOB
    arrival_time_index = arrival_time[service_time.index(shortest_job)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING SHORTEST JOB NUMBER

    if service_time.index(shortest_job) == service_time.index(shortest_job):
        print(f" \nSo therefore process {process[service_time.index(shortest_job)]} will be out of the processes first and will be executed for 0 - {exec_time[service_time.index(shortest_job)]} time length.")

    #calculate the time length for each execution
    sum_time_length = exec_time[service_time.index(shortest_job)]

    #REMOVE ALL CORRRESPONDING INDEX TO SHORTEST JOB INDEX GOTTEN
    process.remove(process_index)
    exec_time.remove(execution_time_index)
    service_time.remove(service_time[service_time.index(shortest_job)])
    arrival_time.remove(arrival_time_index)

    print("______________________________________________________________________________\nprocesses left with their corresponding arrival, execution time and service time; ")
    print(f"\nPROCESS NAME \t ARRIVAL TIME \t\t EXECUTION TIME \t SERVICE TIME")
    for i in range(len(process)):
        print(f'\n {process[i]} \t\t {arrival_time[i]} \t\t\t {exec_time[i]} \t\t\t {service_time[i]}')

        next_shortest_job = min(service_time)

    print(f"\nThe next shortest job for the process is {next_shortest_job}")

    process_index = process[service_time.index(next_shortest_job)] #GET THE PROCESS INDEX FOR THE CORRESPONDING SHORTEST JOB PROCESS NUMBER
    execution_time_index = exec_time[service_time.index(next_shortest_job)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING SHORTEST JOB
    arrival_time_index = arrival_time[service_time.index(next_shortest_job)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING SHORTEST JOB NUMBER

    sum_next_time_length = sum_time_length + exec_time[service_time.index(next_shortest_job)]

    if service_time.index(next_shortest_job) == service_time.index(next_shortest_job):
        print(f" \nSo therefore process {process[service_time.index(next_shortest_job)]} will be out of the processes next and will be executed for {sum_time_length} - {sum_next_time_length} time length.")
    
    #REMOVE ALL CORRRESPONDING INDEX TO SHORTEST JOB INDEX GOTTEN
    process.remove(process_index)
    exec_time.remove(execution_time_index)
    service_time.remove(service_time[service_time.index(next_shortest_job)])
    arrival_time.remove(arrival_time_index)

    print("______________________________________________________________________________\nprocesses left with their corresponding arrival, execution time and service time; ")
    print(f"\nPROCESS NAME \t ARRIVAL TIME \t\t EXECUTION TIME \t SERVICE TIME")
    for i in range(len(process)):
        print(f'\n {process[i]} \t\t {arrival_time[i]} \t\t\t {exec_time[i]} \t\t\t {service_time[i]}')

        next_shortest_job = min(service_time)

    print(f"\nThe next shortest job for the process is {next_shortest_job}")

    process_index = process[service_time.index(next_shortest_job)] #GET THE PROCESS INDEX FOR THE CORRESPONDING SHORTEST JOB PROCESS NUMBER
    execution_time_index = exec_time[service_time.index(next_shortest_job)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING SHORTEST JOB
    arrival_time_index = arrival_time[service_time.index(next_shortest_job)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING SHORTEST JOB NUMBER

    sum_new_time_len = sum_next_time_length + exec_time[service_time.index(next_shortest_job)]

    if service_time.index(next_shortest_job) == service_time.index(next_shortest_job):
        print(f" \nSo therefore process {process[service_time.index(next_shortest_job)]} will be out of the processes next and will be executed for {sum_next_time_length} - {sum_new_time_len} time length.")

    #REMOVE ALL CORRRESPONDING INDEX TO SHORTEST JOB INDEX GOTTEN
    process.remove(process_index)
    exec_time.remove(execution_time_index)
    service_time.remove(service_time[service_time.index(next_shortest_job)])
    arrival_time.remove(arrival_time_index)

    print("______________________________________________________________________________\nprocesses left with their corresponding arrival, execution time and service time; ")
    print(f"\nPROCESS NAME \t ARRIVAL TIME \t\t EXECUTION TIME \t SERVICE TIME")
    for i in range(len(process)):
        print(f'\n {process[i]} \t\t {arrival_time[i]} \t\t\t {exec_time[i]} \t\t\t {service_time[i]}')

        next_shortest_job = min(service_time)

    print(f"\nThe next shortest job for the process is {next_shortest_job}")

    process_index = process[service_time.index(next_shortest_job)] #GET THE PROCESS INDEX FOR THE CORRESPONDING SHORTEST JOB PROCESS NUMBER
    execution_time_index = exec_time[service_time.index(next_shortest_job)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING SHORTEST JOB
    arrival_time_index = arrival_time[service_time.index(next_shortest_job)] #GET THE EXECUTION TIME INDEX FOR THE CORRESPONDING SHORTEST JOB NUMBER

    sum_last_time_len = sum_new_time_len + exec_time[service_time.index(next_shortest_job)]

    if service_time.index(next_shortest_job) == service_time.index(next_shortest_job):
        print(f" \nSo therefore process {process[service_time.index(next_shortest_job)]} will be out of the processes next and will be executed for {sum_new_time_len} - {sum_last_time_len} time length.")

    #REMOVE ALL CORRRESPONDING INDEX TO SHORTEST JOB INDEX GOTTEN
    process.remove(process_index)
    exec_time.remove(execution_time_index)
    service_time.remove(service_time[service_time.index(next_shortest_job)])
    arrival_time.remove(arrival_time_index)

    if exec_time == []:
        print(f'\nAll execution has been completed successfully! \nTotal number of executions = {summation_of_all_exec}')

#execute the program function
if __name__ == "__main__":
    shortest_job_first()
