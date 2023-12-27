# Description: Shortest Job First algorithm

def sjf(processes):
    #sort by execution with same arrival

    head = processes[0].arrival
    result = 0
    for i in range(len(processes)):
        for j in range(i, len(processes), 1):
            if processes[j].arrival <= head:
                if processes[j].execute < processes[i].execute:
                    temp = processes[j].execute
                    processes[j], processes[i] = processes[i], processes[j]
            else:
                break
        processes[i].waiting = head - processes[i].arrival
        result += processes[i].waiting
        head += processes[i].execute
        print(head)

    result = round(result / len(processes), 3)
    processes.append(result)
    print(result)
    return processes