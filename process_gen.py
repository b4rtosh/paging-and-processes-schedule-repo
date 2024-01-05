import secrets
from sjf import sjf
from fcfs import fcfs
import os
import datetime
from tabulate import tabulate


class Process:  # class for processes
    def __init__(self, execute_arg, arrival_arg):
        self.execute = execute_arg
        self.arrival = arrival_arg
        self.waiting = 0


def generate_processes(number, execute_choice, execute, come_choice, arrival):
    # execute_choice and come_choice are booleans - True if random, False if not
    if execute == 1:
        execute_choice = False
    if arrival == 0:
        come_choice = False
    processes = []
    if execute_choice and come_choice:  # generate random processes according to choices
        for i in range(number):
            processes.append(Process(secrets.randbelow(execute) + 1, secrets.randbelow(arrival + 1)))
    elif execute_choice and not come_choice:
        for i in range(number):
            processes.append(Process(secrets.randbelow(execute) + 1, arrival))
    elif not execute_choice and come_choice:
        for i in range(number):
            processes.append(Process(execute, secrets.randbelow(arrival + 1)))
    else:
        for i in range(number):
            processes.append(Process(execute, arrival))
    return processes


def execute_algorithm(processes, choice):   # execute algorithm based on choice
    if choice == "FCFS":
        processes = fcfs(processes)
    else:
        processes = sjf(processes)
    return processes


def save_test(number, random_execute, execute, random_arrival, arrival, algorithm, processes, gen_processes):
    project_path = os.getcwd()  # get current working directory
    if not os.path.exists(project_path + "/scheduling"):
        os.mkdir(project_path + "/scheduling")
    gen_table = []
    for i in range(len(gen_processes)):
        gen_table.append([gen_processes[i].arrival, gen_processes[i].execute])
    result_table = []
    for i in range(len(processes) - 1):
        result_table.append([processes[i].arrival, processes[i].execute, processes[i].waiting])
    # save file with name: algorithm-date.txt
    file_name = algorithm + "_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".txt"
    with open(project_path + "/scheduling/" + file_name, "w") as file:  # open file and write results
        file.write("Test: " + file_name + "\n")
        file.write("Number of processes: " + str(number) + "\n")
        file.write("Arrival: ")
        if random_arrival:
            file.write("random up to " + str(arrival) + "\n")
        else:
            file.write(str(arrival) + "\n")
        file.write("Execution: ")
        if random_execute:
            file.write("random up to " + str(execute) + "\n")
        else:
            file.write(str(execute) + "\n")
        file.write("Algorithm: " + algorithm + "\n")
        file.write("Average waiting time: " + str(processes[-1]) + "\n")
        file.write("Generated processes:\n")
        file.write(tabulate(gen_table, headers=["Arrival", "Execute"], tablefmt="grid") + "\n")
        file.write("Ordered processes:\n")
        file.write(tabulate(result_table, headers=["Arrival", "Execute", "Waiting"], tablefmt="grid"))


def print_processes(processes):
    for i in processes:
        print(i.execute, i.arrival, end='; ')
    print()
