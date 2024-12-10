import pytest
from project import table_of_information, job_cost, discount_in_advance


data = {
    "a": ("Full Mouth Restoration", 250),
    "b": ("Dental Implants", 50),
    "c": ("Teeth Whitening", 100),
    "d": ("General Dentistry", 150),
    "e": ("Crown and Bridgework", 75),
}


def test_table_of_information():
    output = table_of_information(data)
    expected_output = {

        "a": ("Full Mouth Restoration", 250),
        "b": ("Dental Implants", 50),
        "c": ("Teeth Whitening", 100),
        "d": ("General Dentistry", 150),
        "e": ("Crown and Bridgework", 75),
    }

    assert output == expected_output


def test_job_cost():
    assert job_cost("a") == 250
    assert job_cost("b") == 50
    assert job_cost("c") == 100
    assert job_cost("f") == 0


def test_discount_in_advance():
    assert discount_in_advance == "Your amount to pay with discount is: $125.00"
    assert discount_in_advance == 125.0

    assert discount_in_advance == "You have to pay full amount: $250.00"
    assert discount_in_advance == 250.0

    assert discount_in_advance == "Invalid option"
    assert discount_in_advance == 0
