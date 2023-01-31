class BMI:

    def __init__(self, name, age, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age

    def calculate_bmi(self):
        if self.__human():
            return round(self.weight / (self.height * 0.01) ** 2, 3)

    def bmi_index(self):
        if self.calculate_bmi() is not None:
            if self.calculate_bmi() <= 18.5:
                return 'Underweight'
            elif 18.5 <= self.calculate_bmi() <= 24.9:
                return 'Normal Weight'
            elif 25 < self.calculate_bmi() <= 29.9:
                return 'Over Weight'
            else:
                return 'Obese'

    def __human(self):
        if self.height > 240 or self.weight > 200:
            return False
        return True

    def __str__(self):
        return f"NAME: {self.name}\nAge: {self.age}\nHeight: " \
               f"{self.height} cm\nWeight: {self.weight} kgs\nBmi: " \
               f"{self.calculate_bmi()}\nBody Index: {self.bmi_index()}" if \
            self.__human() else 'If you are human, enter Valid Details!'


if __name__ == '__main__':
    print('Whatever you are searching is no longer here')
