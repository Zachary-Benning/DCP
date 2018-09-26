#Implement a job scheduler which takes in a function f and an integer n, and
#calls f after n milliseconds.
from time import sleep


def random_function():
    print("Job Complete")


def job_scheduler(f, x):
    sleep(x * .01)
    random_function()


job_scheduler(random_function, 50)

