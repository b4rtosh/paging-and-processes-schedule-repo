# LRU - Least Recently Used algorithm
# paging algorithm
# memorySize - size of memory
# pageSequence - sequence of pages

def lru(memorySize, pageSequence):
    pageFaults = 0
    memory = []  # used to keep track of the pages in the memory
    result = []  # used to return results
    last_used = []  # used to keep track of the last used page
    for i in range(len(pageSequence)):
        if pageSequence[i] not in memory:
            if len(memory) < memorySize:  # if memory is not full add page to memory
                memory.append(pageSequence[i])
                last_used.append(pageSequence[i])
            else:  # if memory is full replace the least recently
                memory[memory.index(last_used[0])] = pageSequence[i] # find and replace least recently used page in memory
                last_used.pop(0)  # remove page and add new one to the end
                last_used.append(pageSequence[i])
            pageFaults += 1
        else:  # if page is in memory update last_used page and leave memory as it is
            last_used.remove(pageSequence[i])   # remove page from queue and add it to the end
            last_used.append(pageSequence[i])
        # below code is used for results
        result.append(pageSequence[i])
        frames = str()
        for j in range(len(memory)): frames += str(memory[j]) + " "
        result.append(frames)
    result.append(pageFaults)  # add page faults to result for further analysis
    return result
