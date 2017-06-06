import interpolation
import os.path

basepath = os.path.dirname(__file__)

fp = os.path.abspath(os.path.join(
            basepath, "example_data/input_test_data.csv"))

array = interpolation.parseMatrix(fp)
interpolation.interpolateMatrix(array)