"""Tests my dictionary"""

__author__ = "730469212"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


def test_invert_empty():
    """Edge case for invert with empty dictionary"""
    result = invert({})
    assert result == {}


def test_invert_single():
    """use case for invert dictionary with single entry"""
    result = invert({"cat": "tevye"})
    assert result == {"tevye": "cat"}


def test_invert_multiple():
    """use case for invert dictionary with multiple entries"""
    result = invert({"cat": "tevye", "dog": "bonya"})
    assert result == {"tevye": "cat", "bonya": "dog"}


def test_count_empty():
    """edge case for count when list is empty"""
    result = count([])
    assert result == {}


def test_count_single():
    """use case for count when list has one entry"""
    result = count(["Carolina"])
    assert result == {"Carolina": 1}


def test_count_multiple():
    """use case for count when list has multiple entries"""
    result = count(
        [
            "Carolina",
            "Carolina",
            "Carolina",
            "Carolina",
            "Carolina",
            "Carolina",
            "Carolina",
            "Dook",
            "Dook",
            "Dook",
            "Dook",
            "Dook",
        ]
    )
    assert result == {"Carolina": 7, "Dook": 5}


def test_favorite_color_empty():
    """edge case for favorite color with empty dictionary"""
    result = favorite_color({})
    assert result == ""


def test_favorite_color_single():
    """use case for when only one color in list"""
    result = favorite_color({"Caroline": "Orange"})
    assert result == "Orange"


def test_favorite_color_multiple():
    """use case for when multiple colors in list"""
    result = favorite_color({"Caroline": "Orange", "Jessica": "Pink", "Lucy": "Pink"})
    assert result == "Pink"


def test_favorite_color_tie():
    """use case for when the list results in a tie"""
    result = favorite_color({"Caroline": "Orange", "Jessica": "Pink"})
    assert result == "Orange"


def test_bin_len_empty():
    """edge case for bin_len when list is empty"""
    result = bin_len([])
    assert result == {}


def test_bin_len_single():
    """use case for bin_len when list has a single entry"""
    result = bin_len(["Hozier"])
    assert result == {6: {"Hozier"}}


def test_bin_len_multiple():
    """use case for bin_len when list has multiple entries"""
    result = bin_len(["Hozier", "Nirvana", "Clairo", "Joni", "Rihanna"])
    assert result == {4: {"Joni"}, 6: {"Hozier", "Clairo"}, 7: {"Nirvana", "Rihanna"}}
