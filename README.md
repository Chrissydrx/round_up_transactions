# Round-Up Transactions

This project is designed to round up every transaction from a CSV file and sum the rounded amounts. The primary use case is for applications where users want to round up their spending to the nearest whole number and save or donate the difference.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Parse transactions from a CSV file
- Round up each (or specific) transaction to the nearest whole number
- Sum the rounded amounts
- Output the total rounded-up sum

## Requirements

- Python 3.12 or higher
- pandas library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Chrissydrx/round_up_transactions.git
```

2. Change into the project directory:

```bash
cd round-up-transactions
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Change the default values in the `main.py` script to match your preferences. The default values are as follows and match exported transactions from the German bank Commerzbank:

```python
separator = ";"
date_column_name = "Buchungstag"
value_column_name = "Betrag"
only_negative_amounts = True
regex_date = r"\d{2}\.\d{4}"
csv_file = "data/values.csv"
ask_for_file_path = False
```

## Usage

1. Run the script:

```bash
python main.py
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.