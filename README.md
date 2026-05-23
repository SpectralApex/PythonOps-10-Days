# PythonOps — 10 Days Challenge 🐍

A structured Python practice repository focused on improving scripting, automation, logic building, and problem-solving through a 10-day challenge format.

This repository demonstrates consistent hands-on coding practice and progressive Python skill development.

---

## Project Goals

- Strengthen Python fundamentals
- Build scripting discipline
- Practice real-world coding logic
- Improve automation mindset
- Develop operator-style problem solving

---

## Skills Demonstrated

- Python Fundamentals
- Loops & Conditionals
- Functions & Modular Design
- Input Validation
- Algorithmic Thinking
- Scripting Workflows
- Beginner Automation Concepts

---

## Repository Structure

```bash
PythonOps-10-Days/
│
├── Day-01/
├── Day-02/
├── Day-03/
├── Day-04/
├── Day-05/
├── Day-06/
├── Day-07/
├── Day-08/
├── Day-09/
└── Day-10/
```

---

## Setup

Clone the repository:

```bash
git clone https://github.com/SpectralApex/PythonOps-10-Days.git
cd PythonOps-10-Days
```

Run Python files:

```bash
python filename.py
```

---

## Example Challenges

### FizzBuzz

```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

### Prime Number Checker

```python
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True
```

---

## Why This Repository Matters

This repository highlights:

- coding consistency 📈
- progressive skill development
- scripting practice
- logical problem solving
- beginner-to-intermediate Python growth

---

## Future Improvements

- Add advanced automation scripts
- Add networking exercises
- Add file handling modules
- Add API integration projects
- Add cybersecurity-related Python tooling

---

## Author

Created by SpectralApex

---

## License

MIT License
