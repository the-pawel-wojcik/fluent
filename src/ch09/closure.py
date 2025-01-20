def make_average():
    unused_int = 7
    series = []
    def averger(new_val):
        unused_cmplx = 0.7 + 0.7j
        series.append(new_val)
        total = sum(series)
        return total / len(series)
    return averger


avg = make_average()

print(f"{avg(1)=}")
print(f"{avg(2)=}")
print(f"{avg(3)=}")


print(f"{avg.__code__.co_varnames}=")
print(f"{avg.__code__.co_freevars}=")
print(f"{avg.__closure__}=")
print(f"{avg.__closure__[0].cell_contents}=")
