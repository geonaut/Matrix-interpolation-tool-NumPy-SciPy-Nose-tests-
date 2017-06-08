Tool for interpolating missing data in a matrix
===============================================

This tool will use a specified interpolation method to fill in missing values in a matrix. The interpolated values are a function of the neighbouring values.

It is based on Python 3.6. I have put the file in a Python 3 venv, so the Python version is controlled.

Using the code:
===============

Activate the venv: `source venv/bin/activate`
Run the code: `python run.py`
Run the tests: `nosetests`
Run the tests with coverage: `nosetests --with-coverage --cover-erase --cover-package=interpolation_tool --cover-html`

Notes:
======

-  The core interpolation function has a flaw - the interpolation doesn't work where there are <3 adjacent values i.e. at the corners of the matrix.
-  The output of the interpolation function is a .csv file
-  The tool can handle adjacent NaNs

To Do:
======

-  Investigate the 'corner problem', to see if the interpolation can take place for fewer (<3) adjacent values. This is a limitation of the numpy module, and may even be the preferred behaviour.