def days_lived(year_of_birth, age):
    leap_years = (year_of_birth % 4 == 0 and year_of_birth % 100 != 0) or year_of_birth % 400 == 0
    days_in_year = 366 if leap_years else 365
    days_lived = age * days_in_year
    return days_lived


print(days_lived(2003, 19))


