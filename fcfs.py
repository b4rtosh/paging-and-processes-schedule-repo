# FCFS - First Come First Serve algorithm

def fcfs(processes):
    # sort processes by arrival_arg time
    processes.sort(key=lambda x: x.arrival)
    head = processes[0].arrival  # time of simulation execution
    result = 0  # final average waiting time
    for i in range(len(processes)):
        processes[i].waiting = head - processes[i].arrival  # calculate waiting time
        result += processes[i].waiting  # add waiting time to result
        head += processes[i].execute  # add execute time to head
        print(head)
    result = round(result / len(processes), 3)  # calculate average waiting time and round it to 3 decimal places
    processes.append(result)  # add result to list of executed processes
    return processes
