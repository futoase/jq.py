from nose.tools import istest, assert_equal, assert_raises

from jq import jq


@istest
def dot_operator_does_nothing_to_string_input():
    assert_equal(
        "42",
        str(jq(".").transform("42", raw=True))
    )


@istest
def dot_operator_does_nothing_to_json_input():
    assert_equal(
        '"42"',
        str(jq(".").transform("42"))
    )


@istest
def can_add_one_to_each_element_of_an_array():
    assert_equal(
        "[2,3,4]",
        str(jq("[.[]+1]").transform("[1,2,3]", raw=True))
    )


@istest
def output_elements_are_separated_by_newlines():
    assert_equal(
        "1\n2\n3",
        str(jq(".[]").transform("[1,2,3]", raw=True))
    )


@istest
def string_to_json_parses_json_output():
    assert_equal(
        [2, 3, 4],
        jq("[.[]+1]").transform("[1,2,3]", raw=True).json()
    )


@istest
def string_to_json_parses_json_output():
    assert_equal(
        [2, 3, 4],
        jq(".[]+1").transform("[1,2,3]", raw=True).json_all()
    )


@istest
def output_elements_are_separated_by_newlines_when_there_are_multiple_inputs():
    assert_equal(
        "2\n3\n4",
        str(jq(".+1").transform("1\n2\n3", raw=True))
    )


@istest
def value_error_is_raised_if_program_is_invalid():
    assert_raises(ValueError, lambda: jq("!"))
