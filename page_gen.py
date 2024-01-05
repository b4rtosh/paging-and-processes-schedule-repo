import os
import datetime
import secrets
from tabulate import tabulate
from fifo import fifo
from lru import lru


def generate_pages(amount_of_pages, random_pages):
    pages = []
    for i in range(amount_of_pages):
        pages.append(secrets.randbelow(random_pages + 1))
    return pages


def execute_algorithm(memory_size, pages, choice):
    if choice == "FIFO":
        pages = fifo(memory_size, pages)
    else:
        pages = lru(memory_size, pages)
    return pages


def save_test(memory_size, amount, algorithm, max_page, result, sequence):
    project_path = os.getcwd()
    if not os.path.exists(project_path + "/paging"):
        os.mkdir(project_path + "/paging")
    # save file with name: algorithm-date.txt
    file_name = algorithm + "_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".txt"
    result_table = []
    for i in range(0, len(result) - 1, 2):
        result_table.append([result[i], result[i + 1]])
    with open(project_path + "/paging/" + file_name, "w") as file:
        file.write("Test: " + file_name + "\n")
        file.write("Size of memory: " + str(memory_size) + "\n")
        file.write("Amount of pages in sequence: " + str(amount) + "\n")
        file.write("Max page number: " + str(max_page) + "\n")
        file.write("Algorithm: " + algorithm + "\n")
        file.write("Page faults: " + str(result[-1]) + "\n")
        file.write("Sequence: " + str(sequence) + "\n")
        file.write("Results:\n")
        file.write(tabulate(result_table, headers=["Page", "Frame"], tablefmt="grid") + "\n")
