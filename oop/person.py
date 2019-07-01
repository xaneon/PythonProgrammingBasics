class Person:
    def __init__(self, name, alter, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        self.alter = alter

    def getAlter(self):
        return "Das Alter von {} lautet {}.".format(self.name,
                                                    self.alter)
    def __lt__(self, person):
        return self.alter < person.alter

    def __gt__(self, person):
        return self.alter > person.alter

    def __repr__(self):
        return "{} ({})".format(self.name, self.alter)

    def getID(self):
        # id with 8 characters
        id_len = 8
        name = self.name.replace(" ", "").lower()
        if len(name) >= id_len:
            return name[-id_len:]
        else:
            diff = id_len - len(name)
            nums = ""
            for i in range(0, diff):
                nums += str(i)
            return name + nums


if __name__ == '__main__':
    bob = Person('Bob Smith', 33)
    peter = Person('Peter Mo', 34)
    sue = Person('Sue Jones', alter=42, job='dev',
                 pay=100000)
    print(sue.getAlter())
    print(bob < sue)
    print(bob > sue)
    print(bob.getID())
    print(peter.getID())
    print(bob, peter)
