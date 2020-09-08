# get age in years, return age in month
age_in_years = input("How old are you? (in years)")
age_in_months = round(float(age_in_years)*12)
print(f"You are {age_in_months} months old!")

"""
Uri's comments:
==============

* Very good! This code works.
* It's better to add a space in the input after "(in years)", so that the user's
  input will be separated from the last word of the input.
  This is relevant to all your exercises.
* I recommend styling your code according to PEP-8. You can also use PyCharm's
  Code -> Reformat Code feature. For example, spaces around "*".
  This is relevant to all your exercises.
* Here is how your code looks reformatted:

age_in_years = input("How old are you? (in years)")
age_in_months = round(float(age_in_years) * 12)
print(f"You are {age_in_months} months old!")
  
"""
