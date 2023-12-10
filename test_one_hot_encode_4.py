import pytest
from one_hot_encoder import fit_transform


def test_empty_input():
    with pytest.raises(TypeError):
        fit_transform()


def test_simple_input():
    result = fit_transform('a')
    assert len(result) == 1
    assert result[0] == ('a', [1])


def test_multiple_inputs():
    result = fit_transform('a', 'b', 'c', 'a', 'b')
    assert len(result) == 5
    assert result[0] == ('a', [0, 0, 1])


def test_non_string_input():
    result = fit_transform(['a', 'b', 'c'])
    assert len(result) == 3
    assert result[0][0] == 'a'
    assert result[0][1] == [0, 0, 1]


def test_invalid_input():
    with pytest.raises(TypeError):
        fit_transform(1, 2, 3)


def test_duplicate_input():
    result = fit_transform('a', 'b', 'c', 'a', 'b')
    assert len(result) == 5
    assert result[0][0] == 'a'
    assert result[0][1] == [0, 0, 1]
