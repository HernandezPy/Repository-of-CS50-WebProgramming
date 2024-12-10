import pytest
from project import table_of_information, job_cost, discount_in_advance


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


def test_selected_job():
    assert job_cost("a") == "Full Mouth Restoration, 250"
    assert job_cost("b") == "Dental Implants, 50"
    assert job_cost("c") == "Teeth Whitening, 100"


def test_discount_in_advance():
    assert discount_in_advance("a") == 150.0
    assert discount_in_advance("b") == 25.0
    assert discount_in_advance("c") == 50.0
