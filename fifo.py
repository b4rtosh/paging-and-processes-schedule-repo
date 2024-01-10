# FIFO - First In First Out
# paging algorithm
# memorySize - size of memory
# pageSequence - sequence of pages

def fifo(memorySize, pageSequence):
    pageFaults = 0
    memory = []  # used to keep track of the pages in the memory
    result = []  # used to return results
    position = 0  # used to keep track of the last used page
    for i in range(len(pageSequence)):
        if pageSequence[i] not in memory:
            if len(memory) < memorySize:  # if memory is not full add page to memory
                memory.append(pageSequence[i])
            else:  # if memory is full replace the firstly added page with new page
                memory[position] = pageSequence[i]
                position = (position + 1) % memorySize
            pageFaults += 1  # increment page faults
        # if page is in memory leave it as it is
        # below code is used for results
        result.append(pageSequence[i])
        frames = str()
        for j in range(len(memory)): frames += str(memory[j]) + " "
        result.append(frames)
    result.append(pageFaults)  # add page faults to result for further analysis
    return result


