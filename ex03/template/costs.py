# -*- coding: utf-8 -*-
"""Function used to compute the loss."""

import numpy as np

def compute_mse(y, tx, w):
    """Calculate the loss.

    You can calculate the loss using mse or mae.
    """
    n = len(y)
    e = y - np.dot(tx,w)
    return np.dot(np.transpose(e),e)/(2*n)