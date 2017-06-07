import numpy as np
from numpy import genfromtxt
from scipy import interpolate

import os.path

basepath = os.path.dirname(__file__)


def parseMatrix(file):
    """Function for parsing a csv, and converting it to a ndarray

    Args:
        file: csv file

    Returns:
        Returns an n-dimensional numpy array (ndarray)

    """
    array = genfromtxt(file, delimiter=',')

    if not np.isnan(array).any():
        raise ValueError("This array does not contain any 'nan' values")

    return array


def interpolateMatrix(array, int_method='linear'):
    """Function for interpolating missing values in a 2D matrix (ndarray).

    Args:
        matrix: A 2D matrix of data
        int_method: Interpolation method, from interpolate.griddata. One of linear, cubic, nearest.

    Returns:
        Saves a .csv file containing the interpolated array

    """
    if type(array) is not np.ndarray:
        raise ValueError("The array should be an numpy ndarray")

    if int_method is not 'linear':
        if int_method == 'cubic':
            pass
        elif int_method == 'nearest':
            pass
        else:
            raise ValueError(
                "The interpolation method must be one of: linear, cubic, nearest. '%s' is invalid" % int_method)

    # return x axis of array
    x = np.arange(0, array.shape[1])
    # return y axis of array
    y = np.arange(0, array.shape[0])

    # mask NaNs
    array = np.ma.masked_invalid(array)
    # create full grid of x & y values
    xx, yy = np.meshgrid(x, y)

    # flatten to list
    x1 = xx[~array.mask]
    y1 = yy[~array.mask]
    newarr = array[~array.mask]

    interpolated_matrix = interpolate.griddata((x1, y1), newarr.ravel(),
                                               (xx, yy),
                                               method=int_method)

    np.savetxt("output.csv", interpolated_matrix, delimiter=",")
