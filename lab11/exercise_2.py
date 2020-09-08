# get age years, return in months, exception if not num

def get_age_in_years():
    while True:
        try:
            return int(input("How old are you? (in years)"))
        except Exception:
            print("This is not a number :( Please try again")

age_in_months = get_age_in_years()*12
print(f"You are {age_in_months} months old!")

"""
Uri's comments:
==============

* Very good! This code works.
* Formatting - PEP-8 expects 2 blank lines after a function. PyCharm warns
  about it.
  If you use PyCharm's Code -> Reformat Code feature, it will be done automatically.
  
"""
