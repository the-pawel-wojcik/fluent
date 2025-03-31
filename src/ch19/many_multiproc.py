import sys
from time import perf_counter
from typing import NamedTuple
from multiprocessing import Process, SimpleQueue, cpu_count
from multiprocessing import queues

from prime import NUMBERS, is_prime

class primeResult(NamedTuple):
    number: int
    prime: bool
    elapsed: float


JobsQueue = queues.SimpleQueue[int]
ResultsQueue = queues.SimpleQueue[primeResult]


def check(tested_number: int) -> primeResult:
    start = perf_counter()
    prime_test_result = is_prime(tested_number)
    end = perf_counter()
    elapsed = end-start
    return primeResult(tested_number, prime_test_result, elapsed)
    

def worker(jobs: JobsQueue, results: ResultsQueue) -> None:
    while n := jobs.get():
        results.put(check(n))
    results.put(primeResult(0, False, 0.0))


def start_jobs(procs: int, jobs: JobsQueue, results: ResultsQueue) -> None:
    for n in NUMBERS:
        jobs.put(n)

    for _ in range(procs):
        proc = Process(target=worker, args=(jobs, results))
        proc.start()
        jobs.put(0) # "Poison pill"

def report(procs: int, results: ResultsQueue) -> int:
    checked = 0
    procs_done = 0
    while procs_done < procs:
        n, prime, elapsed = results.get()
        if n == 0:
            procs_done += 1
        else:
            checked += 1 
            label = 'P' if prime else ' '
            print(f'{n:16} {label} {elapsed:9.6f} s')

    return checked


def main() -> None:
    if len(sys.argv) < 2:
        procs = cpu_count()
    else:
        procs = int(sys.argv[1])

    print(f'Checking {len(NUMBERS)} numbers with {procs} processes.')
    start = perf_counter()

    jobs: JobsQueue = SimpleQueue()
    results: ResultsQueue = SimpleQueue()

    start_jobs(procs, jobs, results)
    checked = report(procs, results)

    end = perf_counter()
    elapsed = end-start
    print(f'{checked} checks in {elapsed:6.3f} s.')

if __name__ == "__main__":
    main()
