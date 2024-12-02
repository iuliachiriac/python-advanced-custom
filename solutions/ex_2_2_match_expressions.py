# Write a function describe_day that takes an integer representing a day of the
# week (1 for Monday, 2 for Tuesday, etc.) and returns a description of the day.
# Use the match statement to handle the following cases:
#
# If the day is 1, return "Start of the work week".
# If the day is 2, 3, or 4, return "Middle of the work week".
# If the day is 5, return "End of the work week".
# If the day is 6 or 7, return "Weekend".
# For any other value, return "Invalid day".
def describe_day(day):
    match day:
        case 1:
            return "Start of the work week"
        case 2 | 3 | 4:
            return "Middle of the work week"
        case 5:
            return "End of the work week"
        case 6 | 7:
            return "Weekend"
        case _:
            return "Invalid day"


print(describe_day(2))
print(describe_day(6))
print(describe_day(12))


# Write a function that receives a dictionary and, using a match expression,
# returns a tuple (name, age), where name will be either the value under key
# name or the values under first_name and last_name concatenated with a space
# between them, and age will be the value under key age. For any other
# dictionary, it will return a tuple of (None, None). Examples of inputs and
# outputs:

# {"name": "Jane Addams", "age": 23} -> ("Jane Addams", 23)
# {"first_name": "Jane", "last_name": "Addams", "age": 5} -> ("Jane Addams", 5)
# {"hello": 5} -> (None, None)

def get_name_age(user_dict):
    match user_dict:
        case {"name": name, "age": age}:
            return name, age
        case {"first_name": first_name, "last_name": last_name, "age": age}:
            return f"{first_name} {last_name}", age
        case _:
            return None, None


print(get_name_age({"name": "Jane Addams", "age": 23}))
print(get_name_age({"first_name": "Jane", "last_name": "Addams", "age": 5}))
print(get_name_age({"hello": 5}))



# Create a function categorize_date that takes a date object and categorizes it
# based on the month and day. Use the match statement to handle the following
# cases:
#
# If the date is January 1st, return "New Year's Day".
# If the date is December 25th, return "Christmas Day".
# If the date is your birthday, return "My Birthday".
# If the month is December, but not December 25th, return "December".
# If the month is a summer month (June, July, August), return "Summer".
# For any other date, return "Regular day".
from datetime import date


def categorize_date(date_obj):
    match date_obj:
        case date(month=1, day=1):
            return "New Year's Day"
        case date(month=12, day=25):
            return "Christmas Day"
        case date(month=5, day=3):
            return "My Birthday"
        case date(month=12):
            return "December"
        case date(month=6 | 7 | 8):
            return "Summer"
        case _:
            return "Regular day"


print(categorize_date(date.today()))
print(categorize_date(date(2001, 1, 1)))
print(categorize_date(date(1982, 12, 10)))
print(categorize_date(date(1999, 2, 3)))
print(categorize_date(date(1999, 8, 3)))

