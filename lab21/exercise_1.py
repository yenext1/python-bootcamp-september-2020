class Summer():

    def __init__(self):
        self.total = 0

    # Using type hints and sum we can simplify this method
    # Please watch the type hints lesson here for more info:
    # https://www.tocode.co.il/bundles/advanced-python3/lessons/type-hints
    def add(self, *numbers: int):
        self.total += sum(numbers)

    def print_total(self):
        print(self.total)


s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
s.print_total()

# should print 50
t.print_total()

"""
Uri's comments:
==============

* Very good! This code works.
* `def __init__(self):` there is no need for an empty line above it
  and below `class Summer():`.

"""
