from datetime import datetime

date_string = "15-06-2025 14:30:00"
format_code = "%d-%m-%Y %H:%M:%S"

parsed_date = datetime.strptime(date_string, format_code)
print(parsed_date)
# Outputs: 2025-06-15 14:30:00

from datetime import datetime

now = datetime.now()
# Format the date into "Weekday, Month Day, Year"
formatted_string = now.strftime("%d-%m-%Y %H:%M:%S")

print(formatted_string)
# Example Output: 'Monday, June 15, 2025'

