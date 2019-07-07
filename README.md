# pytestDjango

What Is An Automated Test?
- A piece of code which makes sure that another pice of code is working correctly under a certain condition.


Why Should You Test?
- Higher application quality
- Less bugs
- Easier refactoring
- Easier version upgrades


1. Unit Tests
- Test one piece independently of other pieces
- Fastest to run


2. Integration Tests
- Test multiple pieces together to assure that they work well with one another


3. Functional Tests
- Test that everything works from the end-user's point of view
- Slowest to run

# Basic information

- in urls:
path('archive/', views.archive, name='archive-data')

- reverse()
If you need to use something similar to the url template tag in your code.
you can use any of the following to reverse the URL:
//using the named URL
<br/>reverse('archive-data')

- resolve()
The resolve() function can be used for resolving URL paths to the corresponding view functions.
<br/>match = resolve('archive/')


Use of assert
- assert True # nothing happens
<br/>assert 5 > 2

- assert False # exception raise
<br/>assert 2 > 5


Use RequestFactory
- The RequestFactory shares the same API as the test client. 


# Requirement for testing in Python
pip install pytest

pip install pytest-django

pip install pytest-cov

pip install mixer



# In pytest.ini

[pytest]<br/>
DJANGO_SETTINGS_MODULE = project_name.settings<br/>
addopts = --cov --cov-report=html


# To run test and coverage
- py.test
- py.test --cov
