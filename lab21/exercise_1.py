class Summer():

    def __init__(self):
        self.total = 0

    def add(self, *arg):
        for n in arg:
            try:
                self.total += int(n)
            except ValueError:
                print(f"{n} is not a number")

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
