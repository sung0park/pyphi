#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# test/test_distance.py

import numpy as np
import pytest

from pyphi import distance


def test_hamming_matrix():
    answer = np.array([[0, 1, 1, 2, 1, 2, 2, 3],
                       [1, 0, 2, 1, 2, 1, 3, 2],
                       [1, 2, 0, 1, 2, 3, 1, 2],
                       [2, 1, 1, 0, 3, 2, 2, 1],
                       [1, 2, 2, 3, 0, 1, 1, 2],
                       [2, 1, 3, 2, 1, 0, 2, 1],
                       [2, 3, 1, 2, 1, 2, 0, 1],
                       [3, 2, 2, 1, 2, 1, 1, 0]]).astype(float)
    assert np.array_equal(distance._hamming_matrix(3), answer)


def test_large_hamming_matrix():
    n = distance._NUM_PRECOMPUTED_HAMMING_MATRICES + 1
    distance._hamming_matrix(n)


def test_emd_same_distributions():
    a = np.ones((2, 2, 2)) / 8
    b = np.ones((2, 2, 2)) / 8
    assert distance.hamming_emd(a, b) == 0.0


def test_emd_validates_distribution_shapes():
    a = np.ones((2, 2, 2)) / 8
    b = np.ones((3, 3, 3)) / 27
    with pytest.raises(ValueError):
        distance.hamming_emd(a, b)


def test_l1_distance():
    a = np.array([0, 1, 2])
    b = np.array([2, 2, 4.5])
    assert distance.l1(a, b) == 5.5


def test_kld():
    a = np.array([0, 1.0])
    b = np.array([0.5, 0.5])

    assert distance.kld(a, b) == 1
