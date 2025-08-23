import sklearn
from faker import Faker


class HeartDiseaseSuspect:
    def __init__(self):
        fake = Faker()
        self.name = fake.name()
        self.age = 2025 - int(fake.year())
        self.gender = fake.random_element(elements=("M", "F"))
        self.restingHeartRate = fake.pyint(40, 140)
        self.cholesterol = fake.pyint(200, 240)

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nResting Heart Rate: {self.restingHeartRate}\nCholesterol: {self.cholesterol}"


def createSamplePatients(numPatients):
    patients = []

    for i in range(numPatients):
        p = HeartDiseaseSuspect()
        patients.append(p)

    for patient in patients:
        print(patient)
        print("\n")


def main():
    print(f"Using Scikit-Learn version: {sklearn.__version__}")
    createSamplePatients(15)


if __name__ == "__main__":
    main()
