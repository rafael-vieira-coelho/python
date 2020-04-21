"""A simple class."""
class Person(object):
    species = "Homo Sapiens"

    """This is the initializer. It's a special method (see below)."""
    def __init__(self, name):
        self.name = name

    """This method is run when Python tries to cast the object to a string.
     Return this string when using print(), etc. """
    def __str__(self):
        return self.name

    """Reassign and print the name attribute."""
    def rename(self, renamed):
        self.name = renamed
        print("Now my name is {}".format(self.name))


if __name__ == '__main__':
    # Instances
    kelly = Person("Kelly")
    joseph = Person("Joseph")
    john_doe = Person("John Doe")

    # Attributes
    print(kelly.species)
    print(john_doe.species)
    print(joseph.name)

    # Methods
    print(john_doe.__str__())
    print(john_doe)
    john_doe.rename("John")
