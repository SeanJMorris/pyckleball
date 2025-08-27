from datetime import datetime, timedelta
import time
from print_with_color import print_yellow
from utilities.logger import logger


date_format = '%Y-%m-%dT%H:%M:%S%z'
start_message =   "Timer started at--------------------"
stop_message =    "Timer stopped at--------------------"
split_message =   "Timer split check-------------------"
elapsed_message = "Timer total elapsed time------------------------"

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = datetime.now()
        # print_yellow(f"Timer started at:         {self.start_time.strftime(date_format)}")
        formatted_datetime = self.start_time.strftime(date_format)
        logger.warning(start_message + formatted_datetime)
        return self  # Return the instance for use inside the context

    def __exit__(self, exc_type, exc_value, traceback):
        if self.start_time is None:
            print_yellow("Timer has not been started.")
            return
        self.end_time = datetime.now()
        formatted_datetime = self.end_time.strftime(date_format)
        self.get_elapsed_time(self.end_time)
        logger.warning(stop_message + formatted_datetime)

    def split(self):
        if self.start_time is None:
            print_yellow("Timer has not been started.")
            return
        current_time = datetime.now()
        formatted_datetime = current_time.strftime(date_format)
        self.get_elapsed_time(current_time)
        logger.warning(split_message + formatted_datetime)

    def get_elapsed_time(self, elapsed_time_moment):
        if self.start_time is None:
            return "Timer has not been started or stopped."
        elapsed = elapsed_time_moment - self.start_time
        logger.warning(elapsed_message + str(elapsed))

if __name__ == "__main__":
    # timer = Timer()
    # time.sleep(3)
    # timer.stop()

    with Timer() as timer:
        # Simulate some processing time
        time.sleep(2)
        timer.split()
        time.sleep(3)
        # raise Exception("Simulated error for testing.")
        # timer.stop()
