# ☕ Coffee Machine

A command-line coffee machine simulation built in Python. The program manages drink resources, processes coin payments, and dispenses drinks — all through a simple terminal interface.

## Features

- Order from a menu of drinks: **Espresso**, **Latte**, and **Cappuccino**
- Tracks and deducts ingredients (water, milk, coffee) after each order
- Accepts coin input (quarters, dimes, nickles, pennies) and calculates change
- Refunds payment if funds are insufficient
- Reports current resource levels via a secret `report` command
- Machine can be turned off via a secret `off` command

## How to Run

**Requirements:** Python 3.x — no external libraries needed.

```bash
python main.py
```

## Usage

When prompted, type one of the following:

| Input | Action |
|---|---|
| `espresso` | Order an espresso (R1.50) |
| `latte` | Order a latte (R2.50) |
| `cappuccino` | Order a cappuccino (R3.00) |
| `report` | Print current resource levels |
| `off` | Shut down the machine |

## Example

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is R0.0 in change.
Here is your latte ☕. Enjoy!
```

## Project Structure

```
coffee-machine/
│
└── main.py        # All logic in a single procedural script
```

## About

Built as part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**. This project covers functions, dictionaries, loops, and basic input/output handling.
