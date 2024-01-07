# FIFO - First In First Out
# paging algorithm
# memorySize - size of memory
# pageSequence - sequence of pages

def fifo(memorySize, pageSequence):
    pageFaults = 0
    memory = []  # used to keep track of the pages in the memory
    result = []  # used to return results
    last_used = []  # used to keep track of the last used page
    for i in range(len(pageSequence)):
        if pageSequence[i] not in memory:
            if len(memory) < memorySize: # if memory is not full add page to memory
                memory.append(pageSequence[i])
                last_used.append(pageSequence[i])
            else:   # if memory is full replace the firstly added page with new page
                memory[memory.index(last_used[0])] = pageSequence[i]
                last_used.pop(0)    # remove page and add new one to the end
                last_used.append(pageSequence[i])
            pageFaults += 1 # increment page faults
        # if page is in memory leave it as it is
        result.append(pageSequence[i])  # add page and memory to result
        frames = str()
        for j in range(len(memory)): frames += str(memory[j]) + " "
        result.append(frames)
    result.append(pageFaults)   # add page faults to result for further analysis
    return result
