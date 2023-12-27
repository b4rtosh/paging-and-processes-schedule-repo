# Description: First Come First Serve algorithm

def fcfs(processes):
    #print_processes(processes)
    head = processes[0].arrival
    result = 0
    for i in range(len(processes)):
        processes[i].waiting = head - processes[i].arrival
        result += processes[i].waiting
        head += processes[i].execute
        print(head)
    result = round(result / len(processes), 3)
    processes.append(result)
    print(result)
    return processes