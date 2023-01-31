import statistics


class StatisticalSummary(object):
    def __init__(self, seq):
        self.seq = seq

    def five_figure_summary(self, precision=None):
        if precision:
            return (len(self.valid_digits()),
                    self.valid_digits()[1],
                    round(self.extreme_lower(), precision),
                    round(self.extreme_upper(), precision),
                    round(self.lower_quartile(), precision),
                    round(self.median(), precision),
                    round(self.upper_quantile(), precision)
                    )

        return (len(self.valid_digits()), self.valid_digits()[1],
                self.extreme_lower(), self.extreme_upper(),
                self.lower_quartile(), self.median(), self.upper_quantile())

    def valid_digits(self):
        s = [n for n in self.seq if type(n) is int or type(n) is float]
        # print(f'Valid digits- {s}')
        return sorted(s)

    def extreme_lower(self):
        return self.valid_digits()[0]

    def extreme_upper(self):
        return self.valid_digits()[-1]

    def median(self):
        return statistics.median(self.valid_digits())

    def lower_quartile(self):
        return statistics.quantiles(self.valid_digits())[0]

    def upper_quantile(self):
        return statistics.quantiles(self.valid_digits())[2]


if __name__ == '__main__':
    data_0 = range(0, 7)
    data_1 = [29, 17, 24.541043029801116, 72, 14.777908778860523,
              11.052433562201367, 85, 73, 12.796187490669617, 8.164537274737222,
              21, 5.39709745954164, 'into', 'words', 'test', 77,
              28.706727184261982, 67, 50
              ]
    data_3 = [41.13463639477812, 25.96360386982637, 86, 19.272753846489405,
              12.314351848875361, 31, 'test', 4.284315054585646,
              10.075484197701432, 14, 28, 'Random', 43.485161308618046,
              34.654241707233076, 52, 12.934345632825936, 75, 29.735893611992772
              ]
    data_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
              20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 12, 13, 14,
              15, 16, 17, 18, 19, 20, 12, 13, 14, 15, 16, 17, 18, 19, 20, 12,
              13, 14, 15, 16, 17, 18, 19, 20, 16]

    data_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 12, 12, 13, 13, 13, 13,
              14, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 16, 16, 17, 17, 17,
              17, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 20, 20, 21, 22, 23,
              24, 25, 26, 27, 28, 29, 30, 31, 32
              ]

    data_6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(len(data_5))
    print(data_5[len(data_5) // 2])
    print('*' * 90)
    print(list(data_0))
    print(StatisticalSummary(data_0).five_figure_summary(2))
    # print(StatisticalSummary(data_1).five_figure_summary())
    # print(StatisticalSummary(data_3).five_figure_summary())
    print(StatisticalSummary(data_4).five_figure_summary())
    print(len(data_4))
    data_4.sort()
    print(data_4[:15], '\n', data_4[15:30], '\n', data_4[30:45], '\n',
          data_4[45:])
    print(StatisticalSummary(data_5).five_figure_summary())
    print(StatisticalSummary(data_6).five_figure_summary())
