def make_averger():
    count = 0
    total = 0
    def averger(new_val):
        nonlocal count, total
        count += 1
        total += new_val
        return total / count
    return averger


avg = make_averger()
print(f'{avg(2)}=')
print(f'{avg(4)}=')
print(f'{avg(6)}=')
