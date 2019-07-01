class M1:
    def getAttr(self):
        return self.__geheim * 1.5
    def setAttr(self, variable):
        self.__geheim = float(variable) / 2
    eigensch = property(getAttr, setAttr)

class M2:
    def __getAttr(self):
        return self.__geheim * 1.5
    def __setAttr(self, variable):
        self.__geheim = float(variable) / 2
    eigensch = property(__getAttr,
                        __setAttr)

class M3:
    @property
    def eigensch(self):
        return self.__geheim * 1.5
    @eigensch.setter
    def eigensch(self, variable):
        self.__geheim = float(variable) / 2

m1 = M1(); m2 = M2(); m3 = M3()
m1.eigensch = m2.eigensch = m3.eigensch = 4
m1.setAttr(4)  # m2.__setAttr(42) nicht
print(m1.__dict__, m2.__dict__, m3.__dict__)
print(m1.eigensch, m2.eigensch, m3.eigensch)
print(m1.getAttr())  # m2.__getAttr() nicht
print(m1.__dict__, m2.__dict__, m3.__dict__)
