import os
import datetime
import random
from fifo import fifo
from lru import lru


def generate_pages(amount_of_pages, random_pages):
    pages = []
    for i in range(amount_of_pages):
        pages.append(random.randrange(0, random_pages))
    return pages


def execute_algorithm(memory_size, pages, choice):
    if choice == "FIFO":
        pages = fifo(memory_size, pages)
    else:
        pages = lru(memory_size, pages)
    return pages


def save_test(memory_size, amount, algorithm, max_page, result):
    project_path = os.getcwd()
    if not os.path.exists(project_path + "/paging"):
        os.mkdir(project_path + "/paging")
    # save file with name: algorithm-date.txt
    file_name = algorithm + "_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".txt"
    with open(project_path + "/paging/" + file_name, "w") as file:
        file.write("Test: " + file_name + "\n")
        file.write("Number of pages: " + str(amount) + "\n")
        file.write("Size of memory: " + str(memory_size) + "\n")
        file.write("Max page size: " + str(max_page) + "\n")
        file.write("Algorithm: " + algorithm + "\n")
        file.write("Average waiting time: " + str(result[-1]) + "\n")
        file.write("Results: [Page -> Frame]\n")
        for i in range(0, len(result) - 1, 2):
            file.write(str(result[i]) + " -> " + result[i + 1] + "\n")
    print("Test saved as: " + file_name)

