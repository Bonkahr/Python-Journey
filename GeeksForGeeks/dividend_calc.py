class DividendCalculator:
    def __init__(self, ey_alpha_deposit, shares, monthly_contrib, ad_payment,
                 s_payment):
        self.end_of_year_deposits = ey_alpha_deposit
        self.shares = shares
        self.monthly_contribution = monthly_contrib
        self.alpha_deposit_payment = ad_payment / 100
        self.s_payment = s_payment / 100

    def __monthly_deposits_payment(self) -> float:
        total_payment = 0
        for x in range(11, 0, -1):
            total_payment += x / 12 * (self.monthly_contribution *
                                       self.alpha_deposit_payment)
        return total_payment

    def ey_alpha_payment(self) -> float:
        return self.alpha_deposit_payment * self.end_of_year_deposits + \
            self.__monthly_deposits_payment()

    def shares_payment(self) -> float:
        return self.s_payment * self.shares

    def total_dividend(self):
        return self.ey_alpha_payment() + self.shares_payment()

    def payable_dividends(self):
        tax = 0.05 * self.total_dividend()
        return (
            f"""
            --------------------------------------------------------------
            Alpha Deposit payment: Ksh. {self.ey_alpha_payment()}
            Shares Amount:         Ksh  {self.shares_payment()}
            Total dividends:       Ksh. {self.total_dividend()}
            Tax:                   Ksh. {tax}
            ***********************************************************
            Payable Amount:        Ksh. {self.total_dividend() - tax}
            ---------------------------------------------------------------
            """
        )


if __name__ == '__main__':
    end_year_balance = 282000
    deposited_shares = 25000
    monthly_deposits = 6000
    percentage_on_deposits = 11
    percentage_on_shares = 15

    bon = DividendCalculator(end_year_balance, deposited_shares, monthly_deposits,
                             percentage_on_deposits, percentage_on_shares)
    print(bon.payable_dividends())
