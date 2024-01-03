# FIFO - First In First Out
# paging algorithm
# memorySize - size of memory
# pageSequence - sequence of pages

def fifo(memorySize, pageSequence):
    pageFaults = 0
    frame = []  # used to keep track of the pages in the frame
    result = []  # used to return results
    last_used = []  # used to keep track of the last used page
    for i in range(len(pageSequence)):
        if pageSequence[i] not in frame:
            if len(frame) < memorySize: # if frame is not full add page to frame
                frame.append(pageSequence[i])
                last_used.append(pageSequence[i])
            else:   # if frame is full replace the recently used page with new page
                frame[frame.index(last_used[-1])] = pageSequence[i]
                last_used[-1] = pageSequence[i] # update last used page
            pageFaults += 1 # increment page faults
        else:   # if page is in frame update last used page and leve frame as it is
            last_used.remove(pageSequence[i])
            last_used.append(pageSequence[i])
        result.append(pageSequence[i])  # add page and frame to result
        one_frame = str()
        for j in range(len(frame)): one_frame += str(frame[j]) + " "
        result.append(one_frame)
    result.append(pageFaults)   # add page faults to result for further analysis
    return result
