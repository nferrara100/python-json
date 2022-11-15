import pytest
from index import check_grid

def test_no_win(self):
    grid = [[None for y in range(0, 7)] for x in range(0, 6)]
    assert check_grid(grid, 0, 0) == False
