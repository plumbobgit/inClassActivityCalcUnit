import pytest
import calc

# I've included just what the start of some basic code looks like for pytest

def verify_answer(expected, answer, last_answer):
    assert expected == answer
    assert expected == last_answer

def test_add(calc):
    answer = calc.add(2, 2)
    verify_answer(4, answer, calc.last_answer)
