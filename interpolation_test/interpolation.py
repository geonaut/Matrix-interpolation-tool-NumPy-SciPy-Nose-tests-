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


def interpolateMatrix(array, int_method='linear',rescale=False):
    """Function for interpolating missing values in a 2D matrix (ndarray).

    Args:
        matrix: A 2D matrix of data
        int_method: Interpolation method, from interpolate.griddata. One of linear, cubic, nearest. Default is linear.

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

    if rescale is not False:
        if rescale == True:
            pass
        else:
            raise ValueError(
                "You may rescale data e.g. if differences are large. Boolean. Deafult is False. '%s' is invalid" % rescale)

    # Return evenly spaced values within a given interval. 
    # I.e. return x axis of array. 
    # array.shape[1] = columns
    x = np.arange(0, array.shape[1])

    # return y axis of array
    # array.shape[0] = rows
    y = np.arange(0, array.shape[0])

    # mask NaNs in the original array (nan -> --)
    array = np.ma.masked_invalid(array)

    # create full grid of absolute x & y values (i.e. 1D array)
    xx, yy = np.meshgrid(x, y)

    # get the x coordinates from the grid, minus the masks
    x1 = xx[~array.mask]

    # get the y coordinates from the grid, minus the masks
    y1 = yy[~array.mask]

    #get rid of NaNs, and flatten to list
    newarr = array[~array.mask]

    #takes data point coordinates, contiguous flattened masked array, tuple of 1D coordinates, plus interpolation method
    interpolated_matrix = interpolate.griddata((x1, y1), newarr,
                                               (xx, yy),
                                               method=int_method,rescale=False)

    np.savetxt("output.csv", interpolated_matrix, delimiter=",",fmt='%1.6f')
