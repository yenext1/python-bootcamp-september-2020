# Get age in months, return age in years
age_in_months = input("What is your age in months?")
age_in_years = round(int(age_in_months)/12)
print(f"You are {age_in_years} years old!")

"""
Uri's comments:
==============

* Very good! This code works.
* This program rounds an age of 594 to 599 months to 50 years,
  even that this person didn't have their 50th birthday yet.
  Maybe it's better to round down.
  
"""
