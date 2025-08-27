from datetime import datetime, timedelta
import time
from pytz import timezone, utc
from print_with_color import print_blue, print_red

def wait_until_sign_up_moment(sign_up_moment: datetime):
    """
    Wait until the specified sign-up moment.

    :param sign_up_moment: The datetime when the sign-up should occur.
    """
    # ny_tz = timezone("America/New_York")
    current_time = datetime.now(utc)
    time_to_wait = (sign_up_moment - current_time).total_seconds() + 1
    time_to_wait_formatted = f"{round(time_to_wait)}"  # Round to the nearest whole number
    sign_up_moment_formatted = sign_up_moment.strftime('%m/%d/%y %I:%M:%S %p')

    if time_to_wait > 0:
        print_blue(f"Waiting for {time_to_wait_formatted} seconds until sign-up moment at {sign_up_moment_formatted}.")
        time.sleep(time_to_wait)
        print_blue(f"Sign-up moment has arrived----------{sign_up_moment_formatted}.")
    else:
        print_red(f"Sign-up moment {sign_up_moment_formatted} is in the past. No waiting needed.")


if __name__ == "__main__":
    # Example usage
    # sign_up_moment = datetime.now() + timedelta(seconds=10)  # Set to 10 seconds in the future
    # ny_tz = timezone("America/New_York")
    sign_up_moment = datetime(2025, 8, 26, 22, 30).astimezone(utc)
    # print_blue(f"Sign-up moment set for----------------{sign_up_moment.strftime('%m/%d/%y %I:%M:%S %p')}")
    wait_until_sign_up_moment(sign_up_moment)
    print_blue(f"Sign up moment has arrived - it's-----{sign_up_moment.strftime('%m/%d/%y %I:%M:%S %p')}")
