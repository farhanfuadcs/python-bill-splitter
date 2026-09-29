# Python Bill Splitter

A command-line bill-splitting program built with Python. The program calculates the total bill including a tip, divides the cost equally among a group, and determines how much each person owes or should receive based on what they paid.

## Features

* Enter the total bill
* Add a tip percentage
* Calculate the total bill including the tip
* Split the bill equally among multiple people
* Enter how much each person paid
* Calculate how much each person owes
* Calculate how much each person should receive back

## Example

```text
How many people: 3
Total Bill: 60
Tip Percentage: 10

Everyone should pay: 22.00

Person: Fuad
Fuad paid: 22

Person: Rahim
Rahim paid: 30

Person: Karim
Karim paid: 14

Fuad should recieve -0.00
Rahim should recieve 8.00
Karim owes 8.00
```

## Technologies Used

* Python
* Functions
* Loops
* Dictionaries
* Conditional statements
* User input
* Arithmetic calculations

## How to Run

Make sure Python is installed, then run:

```bash
python bill_splitter.py
```

## What I Practiced

This project helped me practice:

* Creating functions with parameters
* Returning values from functions
* Using dictionaries to store results
* Working with `for` and `while` loops
* Validating user input
* Performing percentage calculations
* Formatting decimal values
* Comparing values with conditional statements
* Building a practical command-line application

## How It Works

1. The user enters the number of people.
2. The program asks for the bill amount and tip percentage.
3. The total bill including the tip is calculated.
4. The total is divided equally among everyone.
5. Each person's actual payment is entered.
6. The program compares each payment with their expected share.
7. It displays who owes money and who should receive money.

## Known Limitations

* The bill and tip inputs currently accept only whole numbers.
* The program does not automatically transfer money between people.
* Each person's result is calculated independently.
* Input validation for the amount paid could be improved.
* The program does not handle cases such as entering zero people.

## Future Improvements

* Support decimal bill and tip amounts
* Add better input validation
* Prevent division by zero
* Automatically calculate who should pay whom
* Round results to two decimal places
* Add a graphical interface
* Build a web version
