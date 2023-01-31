class DividendCalculator:

    def __init__(self, initial_amount, monthly_contribution, shares,
                 percentage_return_dividend, percentage_return_shares, tax):
        self.initial_amount = initial_amount
        self.monthly_contribution = monthly_contribution
        self.shares = shares
        self.percentage_return_dividend = percentage_return_dividend / 100
        self.percentage_return_shares = percentage_return_shares / 100
        self.tax = tax / 100

    def _shares_returns(self):
        return self.shares * self.percentage_return_shares

    def _dividend_returns(self):
        initial_return = self.initial_amount * self.percentage_return_dividend

        monthly_returns = 0
        months = list(range(1, 12))
        for month in reversed(months):
            monthly_returns += ((month / 12) * self.monthly_contribution) * \
                               self.percentage_return_dividend
        return initial_return + monthly_returns

    def total_return(self):
        return (1 - self.tax) * (self._shares_returns() +
                                 self._dividend_returns())


if __name__ == '__main__':
    account = DividendCalculator(initial_amount=210231.43,
                                 monthly_contribution=6000,
                                 shares=25000,
                                 percentage_return_shares=14,
                                 percentage_return_dividend=10.75,
                                 tax=5)

    print(f'Your total dividends: {account.total_return():.3f}')
