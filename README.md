# BMI Calculator

A simple Python-based **BMI Calculator** that calculates and classifies BMI for both adults and children. For children, the program uses age- and gender-specific BMI reference values to estimate a BMI percentile and classify the result.

## Features

- Calculates BMI using height and weight.
- Separate BMI calculation for adults and children.
- Accepts age as input to select the appropriate calculation.
- Uses different reference data for boys and girls.
- Estimates BMI percentile for children.
- Classifies child BMI as:
  - Underweight
  - Healthy Weight
  - Overweight
  - Obese
- Allows the user to perform another BMI check.

## Requirements

- Python 3.x
- No external packages are required for the main program.

The program imports `NormalDist` from `statistics` and `math`, although these imports are not directly used in the current version.

## How to Run

1. Make sure Python 3 is installed.
2. Save the Python file.
3. Open a terminal in the folder containing the file.
4. Run:

```bash
python "15:9:26(1).py"
```

## How It Works

### 1. Age Selection

The program first asks for the user's age:

- **20 years or older:** Adult BMI calculation.
- **3–19 years:** Child BMI calculation.
- **2 years or younger:** BMI is not calculated by the program.

### 2. Adult BMI

For adults, BMI is calculated using:

```text
BMI = weight (kg) / height² (m)
```

The program then classifies the BMI according to the ranges implemented in the code:

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5–24.5 | Fit |
| 24.6–29.9 | Overweight |
| Above 30 | Obese |

### 3. Child BMI

For children, the program asks for:

- Gender
- Height in metres
- Weight in kilograms
- Age

It then calculates BMI and selects the corresponding reference values from separate `boys` and `girls` dictionaries.

Each age has four reference values:

```text
p5, p50, p85, p95
```

These are used to estimate the child's BMI percentile.

### 4. Child BMI Categories

The program assigns categories based on the calculated percentile:

| Percentile | Category |
|---|---|
| Below 5th percentile | Underweight |
| 5th–84th percentile | Healthy Weight |
| 85th–94th percentile | Overweight |
| 95th percentile and above | Obese |

## Example

A typical run begins with:

```text
Welcome to BMI calculator.
Enter you age :
```

For a child, the program additionally asks:

```text
Enter whether you are a boy or a girl :
Enter your height in m :
Enter your weight in kg :
Please enter your age again. :
```

The program then calculates BMI, estimates the percentile, and displays the corresponding category.

## Program Structure

The program is organized into three main functions:

### `intro()`

Starts the program and decides whether the user should use the adult or child BMI calculator.

### `bmi_adult()`

Calculates and classifies BMI for users aged 20 or above.

### `bmi_child()`

Calculates BMI for children and uses the stored age- and gender-specific reference data to estimate BMI percentile and category.

## Data Used

The child calculator contains separate BMI reference dictionaries for:

- Boys aged 2–19
- Girls aged 2–19

Each age contains four values representing the reference points used by the program.

## Limitations

- The program requires gender to be entered exactly as `boy` or `girl`.
- Height and weight validation is limited in the current version.
- The adult BMI categories are based on the ranges implemented in this code.
- The child percentile calculation is an estimation using linear interpolation between stored reference points.
- The program is intended as an educational programming project and should not be treated as a medical diagnosis.

## Technologies Used

- **Python 3**
- Functions
- Dictionaries
- Conditional statements
- User input/output
- Arithmetic calculations
- Basic percentile interpolation

## Author

**ANIRUDH THAKUR**

## Project Purpose

This project demonstrates how Python can be used to create a simple health-related calculator while applying fundamental programming concepts such as functions, dictionaries, conditional logic, user input, and mathematical calculations.
