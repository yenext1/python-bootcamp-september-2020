class Widget:

    def __init__(self, name):
        self.name = name
        self.built = False
        self.dependencies = []

    def add_dependency(self, *arg):
        for d in arg:
            self.dependencies.append(d)

    def build(self):
        self.built = True
        for dependency in self.dependencies:
            if not dependency.built:
                dependency.build()
        print(self.name)



luke = Widget("Luke")
hansolo = Widget("Han Solo")
leia = Widget("Leia")
yoda = Widget("Yoda")
padme = Widget("Padme Amidala")
anakin = Widget("Anakin Skywalker")
obi = Widget("Obi-Wan")
darth = Widget("Darth Vader")
_all = Widget("")

luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
_all.build()
# code should print: Han Solo, Padme Amidala, Anakin Skywalker, Leia, Yoda, Luke, Obi-Wan, Darth Vader
# (can print with newlines in between modules)

"""
Uri's comments:
==============

* Very good! This code works.
* `def __init__(self, name):` there is no need for an empty line above it
  and below `class Widget:`.

"""
