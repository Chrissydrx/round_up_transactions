import pandas as pd
import re

separator = ";"
date_column_name = "Buchungstag"
value_column_name = "Betrag"
only_negative_amounts = True
regex_date = r"\d{2}\.\d{4}"
csv_file = "data/values.csv"


def main():
    df = pd.read_csv(csv_file, sep=separator)

    # Get month to filter for
    # date = input("Enter a month with a year: ")
    date = "04.2024"
    if not re.match(regex_date, date):
        print("Invalid date format.")
        return

    # Filter df for dates
    df = df[df[date_column_name].str.contains(date)]

    # Iterate over all rows and sum the difference for each row when rounding the amount up to the nearest euro / dollar.
    sum = 0
    for index, row in df.iterrows():
        amount = float(row[value_column_name].replace(",", "."))
        amount *= 100

        if only_negative_amounts and amount > 0:
            continue

        amount = int(abs(amount))

        amount = amount % 100

        if amount == 0:
            continue

        sum += 100 - amount

    sum /= 100

    print("Sum: " + str(sum))


if __name__ == "__main__":
    main()
