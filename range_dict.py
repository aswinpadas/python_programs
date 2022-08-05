"""Hacker rank 30 Days of CodeDay 12: Inheritance and range in dict()"""


class Person:

    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    grade = {
        range(90, 101): "O",
        range(80, 90): "E",
        range(70, 80): "A",
        range(55, 70): "P",
        range(40, 55): "D",
        range(0, 40): "T",
    }

    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.avg = int(sum(scores) / len(scores))

    def calculate(self):
        return "".join([y for x, y in self.grade.items() if self.avg in x])


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python

scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
