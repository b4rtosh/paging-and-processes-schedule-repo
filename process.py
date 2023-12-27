import random
from sjf import sjf
from fcfs import fcfs
import os
import datetime


class Process:
    def __init__(self, execute_arg, arrival):
        self.execute = execute_arg
        self.arrival = arrival
        self.waiting = 0


def generate_processes(number, execute_choice, execute, come_choice, arrival):
    # execute_choice and come_choice are booleans - True if random, False if not
    if execute == 1:
        execute_choice = False
    if arrival == 0:
        come_choice = False
    processes = []
    if execute_choice and come_choice:
        for i in range(number):
            processes.append(Process(random.randrange(1, execute), random.randrange(0, arrival)))
    elif execute_choice and not come_choice:
        for i in range(number):
            processes.append(Process(random.randrange(1, execute), arrival))
    elif not execute_choice and come_choice:
        for i in range(number):
            processes.append(Process(execute, random.randrange(0, arrival)))
    else:
        for i in range(number):
            processes.append(Process(execute, arrival))
    processes.sort(key=lambda x: x.arrival)
    return processes


def execute_algorithm(processes, choice):
    if choice == "FCFS":
        processes = fcfs(processes)
    else:
        processes = sjf(processes)
    return processes


def save_test(number, random_execute, execute, random_arrival, arrival, algorithm, processes):
    project_path = os.getcwd()
    if not os.path.exists(project_path + "/tests"):
        os.mkdir(project_path + "/tests")
    # save file with name: algorithm-date.txt
    file_name = algorithm + "_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".txt"
    with open(project_path + "/tests/" + file_name, "w") as file:
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
        file.write("Processes: [Order - Arrival - Execute - Waiting]\n")
        for i in range(len(processes) - 1):
            file.write(str(i) + " - " + str(processes[i].arrival) + " - " + str(processes[i].execute) + " - " + str(
                processes[i].waiting) + "\n")


def print_processes(processes):
    for i in processes:
        print(i.execute, i.arrival, end='; ')
    print()
