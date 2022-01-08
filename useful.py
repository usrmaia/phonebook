from implements_db import count_lines

def decrement(page):
    if page > 1:
        return page - 1
    return page

def increment(page):
    count_page = count_lines() / 5
    if page < count_page:
        return page + 1
    return page