import contextlib
import os
import sqlite3
import time
from contextlib import contextmanager

# contextlib contains more utilities than the ones presented above. Take a look
# at suppress and write a code block that uses it.
with contextlib.suppress(FileExistsError):
    os.mkdir("test_dir")


# Create a context manager to measure the time taken by a block of code. Do it
# with both methods presented here (function and class based context managers).
@contextmanager
def measure_time():
    time_start = time.time()
    try:
        yield
    finally:
        time_diff = time.time() - time_start
        print(f"Execution took {time_diff:.4f}s")


class MeasureTime:
    def __init__(self, unit="s"):
        if unit not in ("s", "ms"):
            raise ValueError("Unexpected time unit. Supported values: s, ms.")
        self.unit = unit

    def __enter__(self):
        self.time_start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        time_diff = time.time() - self.time_start
        if self.unit == "ms":  # if unit is milliseconds
            time_diff *= 1000
        print(f"Execution took {time_diff:.4f}{self.unit}")


with measure_time():
    for i in range(2000):
        for j in range(2000):
            prod = i * j
            # if i == 1900:
            #     raise Exception


with MeasureTime("ms"):
    for i in range(2000):
        for j in range(2000):
            prod = i * j


# Create a context manager that opens a file for writing when entering the
# context, writes a default message to the file and ensures the file is closed
# properly when exiting the context.
class FileWriter:
    def __init__(self, filename, author="John Doe"):
        self.filename = filename
        self.author = author

    def __enter__(self):
        self.file = open(self.filename, "w")
        self.file.write(f"--- Written by {self.author} ---\n")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileWriter("new_file.txt", "Jane Smith") as f:
    f.write("Hello world!")
