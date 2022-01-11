from implements_db import count_lines
from tqdm import tqdm
from time import sleep

def decrement(page):
    if page > 1:
        return page - 1
    return page

def increment(page):
    count_page = count_lines() / 5
    if page <= count_page:
        return page + 1
    return page

def progress_bar():
    print("Loading Data Base...")
    for i in tqdm(range(0, 2)):
        sleep(1)