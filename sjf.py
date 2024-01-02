# Description: Shortest Job First algorithm

def sjf(processes):
    # sort by arrival time
    processes.sort(key=lambda x: x.arrival)
    head = processes[0].arrival  # time of simulation execution
    result = 0  # final average waiting time
    for i in range(len(processes)):
        for j in range(i, len(processes), 1):  # sort by execute time if arrival time is less then head
            if processes[j].arrival <= head:
                if processes[j].execute < processes[i].execute:  # swap processes if execute time is less
                    processes[j], processes[i] = processes[i], processes[j]
            else:
                break
        processes[i].waiting = head - processes[i].arrival  # calculate waiting time
        result += processes[i].waiting  # add waiting time to result
        head += processes[i].execute    # add execute time to head
        print(head)
    result = round(result / len(processes), 3)  # calculate average waiting time and round it to 3 decimal places
    processes.append(result)    # add result to list of executed processes
    return processes
