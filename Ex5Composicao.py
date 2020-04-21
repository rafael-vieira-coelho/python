class Person(object):
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name


class City(object):
    def __init__(self, numPeople):
        self.people = []
        self.numPeople = numPeople

    def add_person(self, person):
        self.people.append(person)
        self.numPeople += 1


class Country(object):
    def __init__(self):
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)

    def people_in_my_country(self):
        x = 0
        for c in self.cities:
            x += c.numPeople
        return x


if __name__ == '__main__':
    p1 = Person(1, "Joe")
    p2 = Person(2, "Mary")
    NYC = City(998)
    NYC.add_person(p1)
    NYC.add_person(p2)
    US = Country()
    US.add_city(NYC)
    print(US.people_in_my_country())
