def hash_string(s):
    hash = 0
    for character in s:
        hash = hash * 31 + (ord(character) % 255)
    return hash


def rehash(table, load, capacity):
    c = capacity * 2
    t = [[] for _ in range(c)]
    i = 0
    for bucket in table:
        for e in bucket:
            t, i, c = insert(t, e, i, c)
    return t, i, c


def insert(table, value, load, capacity):
    if load / capacity >= 0.9: # keep load factor less than 0.9
        table, load, capacity = rehash(table, load, capacity)
    bucket = table[hash_string(value) % capacity]
    bucket.append(value) 
    return table, load + 1, capacity


def contains(table, value):
    bucket = table[hash_string(value) % capacity]
    for e in bucket:
        if e == value:
            return True
    return False


def remove(table, value, load, capacity):
    bucket = table[hash_string(value) % capacity]
    bucket.remove(value)
    return table, load - 1, capacity


table = [[]]
capacity = 1
load = 0

words = """This paragraph contains some duplicate words. The
duplicated words will be removed as the program runs. We
generally want our algorithm to avoid putting more than one word
into a single bucket. We can heuristically guarantee this by
randomly selecting a new set of constants for the hashing
function each time.""".split()

for value in words:
    if contains(table, value):
        table, load, capacity = remove(table, value, load, capacity)
    else:
        table, load, capacity = insert(table, value, load, capacity)
    print(table)
    print()
print(load)
print(capacity)
