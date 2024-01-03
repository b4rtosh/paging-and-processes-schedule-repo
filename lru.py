# LRU - Least Recently Used algorithm
# paging algorithm
# memorySize - size of memory
# pageSequence - sequence of pages

def lru(memorySize, pageSequence):
    pageFaults = 0
    frame = []  # used to keep track of the pages in the frame
    result = []  # used to return results
    last_used = []  # used to keep track of the last used page
    for i in range(len(pageSequence)):
        if pageSequence[i] not in frame:
            if len(frame) < memorySize:  # if frame is not full add page to frame
                frame.append(pageSequence[i])
                last_used.append(pageSequence[i])
            else:  # if frame is full replace the least recently
                frame[frame.index(last_used[0])] = pageSequence[i]  # find and replace least recently used page in frame
                last_used.pop(0)  # remove page and add new one to the end of the list
                last_used.append(pageSequence[i])
            pageFaults += 1
        else:  # if page is in frame update last used page and leave frame as it is
            last_used.remove(pageSequence[i])
            last_used.append(pageSequence[i])
        result.append(pageSequence[i])  # add page and frame to result
        one_frame = str()
        for j in range(len(frame)): one_frame += str(frame[j]) + " "
        result.append(one_frame)
    result.append(pageFaults)  # add page faults to result for further analysis
    return result
