### Requirements

I have used Pytest, Selenium and Firefox browser, so only these two external dependencies and browser are required to successfully run test cases. 

### Installation

```python
git clone https://github.com/abek101/Automation-Technical-Test.git
cd Automation-Technical-Test
pip install -r requirements.txt
```

### Execute test cases

To execute all test cases just run pytest in project folder

```python
pytest
```

To execute all test cases in a particular class, change CLASS_NAME to desired class name and run the command in project folder.

```python
pytest -v test_cases/smoke_test.py::CLASS_NAME
```

To execute particular test case, change CLASS_NAME and TEST_CASE_NAME to desired class name and its test case and run the command in project folder.

```python
pytest -v test_cases/smoke_test.py::CLASS_NAME::TEST_CASE_NAME
```
