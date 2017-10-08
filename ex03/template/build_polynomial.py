# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    phi = []
    for i in range(0,degree+1):
        phi = np.append(phi,[np.power(x, i)])
    return np.transpose(np.reshape(phi,(degree+1,len(x))))
