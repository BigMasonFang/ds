# reference Data Structures and Algorithms in Python 2013
from typing import List
import ctypes


class ArrayList:
    def __init__(self) -> None:
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        pass