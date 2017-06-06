Genomics PLC Technical Test
===========================

Based on Python 3.6. I have put the file in a Python 3 venv, so the Python version is controlled.

Using the code:
===============

Activate the venv: `source venv/bin/activate`
Run the code: `python run.py`
Run the tests: `nosetests`
Run the tests with coverage: `nosetests --with-coverage --cover-erase --cover-package=interpolation_test --cover-html`

Notes:
======

-  The core interpolation function has a flaw - the interpolation doesn't work where there are <3 adjacent values. I started to investigate this issue, but as this was a time limited exercise, I decided to move on to other parts of the test. (See to do)
-  The output of the interpolation function is a .csv file
-  The readme asked for both unit tests and UAT tests, however, I found there to be quite a lot of overlap between them, so I decided to focus on writing a more comprehensive suite of unit tests. Normally, I would aim for ~90% code coverage on the unit tests, and write UAT tests against the original specifications.
-  I used nose to run the tests
-  I used the coverage module to generate a code coverage report.
-  I used Git to create a repo
-  I used Jupyter for the initial exploration, and submlime for the final code.
-  I used a ST3 plugin for PEP8 formatting

To Do:
======

-  I started to look at the 'adjacent missing files problem', but didn't get time to implement it. I found this [SO](https://stackoverflow.com/questions/37662180/interpolate-missing-values-2d-python) question that has an approach.
-  Investigate the 'corner problem', to see if the interpolation can take place for fewer (<3) adjacent values