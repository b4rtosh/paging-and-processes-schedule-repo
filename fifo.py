# FIFO - First In First Out
# paging algorithm
# memorySize - size of memory
# pageSequence - sequence of pages

def fifo(memorySize, pageSequence):
    pageFaults = 0
    frame = []  #used to keep track of the pages in the frame
    result = []  # used to return results
    last_used = []  # used to keep track of the last used page
    for i in range(len(pageSequence)):
        if pageSequence[i] not in frame:
            if len(frame) < memorySize:
                frame.append(pageSequence[i])
                last_used.append(pageSequence[i])
            else:
                frame[frame.index(last_used[-1])] = pageSequence[i]
                last_used[-1] = pageSequence[i]
            pageFaults += 1
        else:
            last_used.remove(pageSequence[i])
            last_used.append(pageSequence[i])
        result.append(pageSequence[i])
        one_frame = str()
        for j in range(len(frame)): one_frame += str(frame[j]) + " "
        result.append(one_frame)
    print("Page Faults: ", pageFaults)
    result.append(pageFaults)
    return result
