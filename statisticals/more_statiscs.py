class MyStatistics:

    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

    def population_variance(self):
        return sum([(s - self.mean()) ** 2 for s in self.data]) / len(
            self.data)

    def sample_variance(self):
        return sum([(s - self.mean()) ** 2 for s in self.data]) / (len(
            self.data) - 1)

    def population_standard_deviation(self):
        return self.population_variance() ** 0.5

    def sample_standard_deviation(self):
        return self.sample_variance() ** 0.5

    def population_coefficient_deviations(self):
        return self.population_standard_deviation() / self.mean()

    def sample_coefficient_deviation(self):
        return self.sample_standard_deviation() / self.mean()

    def median(self):
        self.data = sorted(self.data)
        if len(self.data) % 2 != 0:
            return self.data[int((len(self.data)) // 2)]
        else:
            return (self.data[(len(self.data) // 2)] +
                    self.data[(len(self.data) // 2) - 1]) / 2

    def add_data(self, data):
        self.data.extend(data)


if __name__ == '__main__':
    my_data = MyStatistics([1, 2, 5, 3, 7, 9, 12, 13])
    print(my_data.mean())
    print(my_data.sample_variance())
    print(my_data.sample_standard_deviation())
    print(my_data.median())
    my_data.add_data([5, 6, 7, 8, 89, 43, 56])
    print(my_data.sample_standard_deviation())
    print(my_data.sample_variance())
    print(my_data.data)
