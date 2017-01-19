"""
This is just a simple program that helps determine how much money
I would get to keep if I were to win a lottery.

 2017 Federal Tax Bracket
 -------------------------------
 1. 0      to 9325         10%
 2. 9325   to 37950        15%
 3. 37950  to 91900        25%
 4. 91900  to 191650       28%
 5. 191650 to 416700       33%
 6. 416700 to 418400       35%
 7. 418400 to unlimited    39.6%
"""
from collections import OrderedDict

_tax_bracket = {
    0: 0.10,
    9325: 0.15,
    37950: 0.25,
    91900: 0.28,
    191650: 0.33,
    416700: 0.35,
    418400: 0.396,
}

tax_bracket = OrderedDict(sorted(_tax_bracket.items(), key=lambda x: x[0]))


def lottery_tax(winnings):
    if winnings < 0:
        raise ValueError("Can't have negative winnings.")

    tax_bracket = OrderedDict(sorted(_tax_bracket.items(), key=lambda x: x[0]))
    brac_range = list(tax_bracket.keys())
    taxes = []
    for brack_pos in range(len(brac_range) - 1):
        taxes.append(brac_range[brack_pos + 1] - brac_range[brack_pos])

    brac_percent = list(tax_bracket.values())

    max_taxes = []
    for taxed, percent in zip(taxes, brac_percent):
        max_taxes.append(taxed * percent)

    found_flag = False
    total_tax = 0
    while found_flag is not True:
        curr_bracket = brac_range.pop()
        curr_percent = brac_percent.pop()
        if winnings >= curr_bracket:
            total_tax = (winnings - curr_bracket) * curr_percent
            total_tax += sum(max_taxes)
            found_flag = True
        else:
            max_taxes.pop()

    return total_tax
