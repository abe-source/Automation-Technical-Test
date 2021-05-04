# Untitled

### Requirements

I have used Pytest, Selenium and Firefox browser, so only these two external dependencies and browser is required to successfully run test cases. 

### Installation

```python
git clone 
cd
pip install -r requirements.txt
```

### Execute test cases

To execute all test cases just run pytest in project folder

```python
pytest
```

To execute all test cases in a particular class, change <class name> to desired class name and run the command in project folder.

```python
pytest -v test_cases/smoke_test.py::<class name>
```

To execute particular test case, change <class name> and <test case name> to desired class name and its test case and run the command in project folder.

```python
pytest -v test_cases/smoke_test.py::<class name>::<test case name>
```