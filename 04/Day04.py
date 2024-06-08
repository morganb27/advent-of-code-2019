from collections import Counter

def sum_correct_passwords():
    res1 = 0
    res2 = 0
    for i in range(172930, 683083):
        password = str(i)
        if is_valid_password(password):
            res1 += 1
        if is_increasing(password) and has_duplicate_part_two(password):
            res2+=1
    return (res1, res2)

def is_increasing(p):
    for i in range(len(p) - 1):
        if p[i] > p[i+1]:
            return False
    return True

def is_valid_password(p):
    return is_increasing(p) and has_duplicate(p)

def has_duplicate(p):
    return len(p) != len(set(p))

def has_duplicate_part_two(p):
    counter = Counter(p)
    for value in counter.values():
        if value == 2:
            return True
    return False

print(sum_correct_passwords())