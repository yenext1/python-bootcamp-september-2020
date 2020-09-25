from __future__ import annotations
class Widget:
    def __init__(self, name):
        self.name = name
        self.built = False
        self.dependencies = []

    # Using type hints and += we can simplify this method
    # Please watch the type hints lesson here for more info:
    # https://www.tocode.co.il/bundles/advanced-python3/lessons/type-hints
    # Note that because I use Widget as a type hint, and it hasn't been fully defined yet
    # (we're in Widget class definitions now)
    # I had to add the "from __future__ import annotations" statement to the
    # top of the file
    def add_dependency(self, *widgets: Widget):
        self.dependencies += widgets

    def build(self):
        self.built = True
        for dependency in self.dependencies:
            # I prefer to have the "important" part aligned with the loop,
            # so I would write:
            if dependency.built: continue

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
