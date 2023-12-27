# FIFO - First In First Out
# paging algorithm
# memorySize - size of memory
# pageSequence - sequence of pages

def fifo(memorySize, pageSequence):
    pageFaults = 0
    frame = []
    result = []
    for i in range(len(pageSequence)):
        if pageSequence[i] not in frame:
            if len(frame) < memorySize:
                frame.append(pageSequence[i])
            else:
                frame.pop(-1)
                frame.append(pageSequence[i])
            pageFaults += 1
        else:
            frame.remove(pageSequence[i])
            frame.append(pageSequence[i])
        result.append(pageSequence[i])
        one_frame = str()
        for j in range(len(frame)): one_frame += str(frame[j]) + " "
        result.append(one_frame)
    print("Page Faults: ", pageFaults)
    result.append(pageFaults)
    return result
