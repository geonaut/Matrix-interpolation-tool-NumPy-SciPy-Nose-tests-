import unittest
import interpolation
import numpy as np
from numpy import genfromtxt
import sys
import os.path

nan = np.nan
basepath = os.path.dirname(__file__)

sparse_array = np.array([[37.454012, 95.071431, 73.199394, 59.865848, nan],
                         [15.599452, 5.808361, 86.617615, 60.111501, 70.807258],
                         [2.058449, 96.990985, nan, 21.233911, 18.182497],
                         [nan, 30.424224, 52.475643, 43.194502, 29.122914],
                         [61.185289, 13.949386, 29.214465, nan, 45.606998]
                         ])

output_array = np.array([[37.454012, 95.071431, 73.199394, 59.865848, nan],
                         [15.599452, 5.808361, 86.617615, 60.111501, 70.807258],
                         [2.058449, 96.990985, 59.112448, 21.233911, 18.182497],
                         [31.621869, 30.424224, 52.475643, 43.194502, 29.122914],
                         [61.185289, 13.949386, 29.214465, 37.4107315, 45.606998]])


class TestInterpolation(unittest.TestCase):

    def test_parseMatrix_ok(self):

        fp = os.path.abspath(os.path.join(
            basepath, "..", "example_data/input_test_data.csv"))

        result = interpolation.parseMatrix(fp)
        raw = genfromtxt(fp, delimiter=',')

        np.testing.assert_array_equal(raw, result)

    def test_parseMatrix_no_missing(self):

        fp = os.path.abspath(os.path.join(
            basepath, "..", "example_data/interpolated_test_data.csv"))

        with self.assertRaises(ValueError) as context:
            interpolation.parseMatrix(fp)

        self.assertTrue(
            "This array does not contain any 'nan' values" in str(context.exception))

    def test_interpolateMatrix_ok(self):

        interpolation.interpolateMatrix(sparse_array)

        fp = os.path.abspath(os.path.join(
            basepath, "..", "output.csv"))

        raw = genfromtxt(fp, delimiter=',')

        np.testing.assert_array_equal(output_array, raw)

    def test_interpolateMatrix_not_ndarray(self):

        test_list = [1, 2, 3]

        with self.assertRaises(ValueError) as context:
            interpolation.interpolateMatrix(test_list)

        self.assertTrue(
            "The array should be an numpy ndarray" in str(context.exception))

    def test_interpolateMatrix_invalid_method(self):

        with self.assertRaises(ValueError) as context:
            interpolation.interpolateMatrix(sparse_array,int_method="test")

        self.assertTrue(
            "The interpolation method must be one of: linear, cubic, nearest. 'test' is invalid" in str(context.exception))

if __name__ == '__main__':
    unittest.main()
