from datetime import datetime
from pytz import timezone, utc
from print_with_color import print_blue


ny_tz = timezone("America/New_York")
case_day_ny_tz = datetime.now().astimezone(ny_tz)
case_day_from_this_computer = datetime.now().astimezone(utc)

case_day_ny_tz_formatted = datetime.now().astimezone(ny_tz)
case_day_utc = datetime.now().astimezone(utc)


def datetime_formatter(datetime_input: datetime) -> str:
    # date_string_to_print = datetime_input.strftime('%Y-%m-%d %I:%M %p %Z')
    # produce string in this format: Tue, 26 Aug 2025 01:54:04 GMT
    date_string_to_print = datetime_input.strftime('%a, %d %b %Y %I:%M:%S %Z')
    return date_string_to_print

print_blue(f"case_day_ny_tz:--------------------------------{datetime_formatter(case_day_ny_tz)}")
print_blue(f"case_day_utc:----------------------------------{datetime_formatter(case_day_utc)}")


case_day_utc_for_yml = case_day_utc.strftime('%a, %b %-d @ %-I:%M')
my_utc_string_cron = case_day_utc.strftime('%-M %-H * * *')
print_blue("Chron format...................................min hr day_of_month month day_of_week")
print_blue("Chron format...................................m_ h_ d m d")
print_blue(f"Right now UTC time in cron format:-------------{my_utc_string_cron}")

moment_to_run_yml_file_ny_tz = datetime(2025, 8, 26, 16, 0).astimezone(ny_tz)
moment_to_run_yml_file_utc = moment_to_run_yml_file_ny_tz.astimezone(utc)
print_blue(f"I'm expecting this script to run at nytz: {datetime_formatter(moment_to_run_yml_file_ny_tz)}")
print_blue(f"I'm expecting this script to run at utc: {datetime_formatter(moment_to_run_yml_file_utc)}")
