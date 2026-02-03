# Day 1: Data-Driven Login Tests

## Description
Automated login tests using data-driven approach with CSV file containing multiple user credentials.

## Skills Demonstrated
- Data-driven testing with pytest parametrize
- CSV file handling
- Multiple test scenarios
- Clean test organization

## Technologies
- Python 3.13
- Selenium WebDriver
- Pytest
- CSV module

## Test Data
Tests 6 different user scenarios from `test_data/users.csv`:
- Valid users
- Locked users
- Invalid credentials

## How to Run
```bash
pytest tests/test_login_data_driven.py -v
```

## Results
- 6 test cases executed
- 100% pass rate
