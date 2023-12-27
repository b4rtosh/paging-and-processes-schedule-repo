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
    if choice == "FIFO"
        pages = fifo(memory_size, pages)
    else
        pages = lru(memory_size, pages)
    return pages

