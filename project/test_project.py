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
    expected_output = [
        "Customer Services Available",
        "a: Full Mouth Restoration - $250",
        "b: Dental Implants - $50",
        "c: Teeth Whitening - $100",
        "d: General Dentistry - $150",
        "e: Crown and Bridgework - $75"
    ]
    assert output == expected_output


def test_job_cost():
    assert job_cost(data, "a") == 250
    assert job_cost(data, "b") == 50
    assert job_cost(data, "c") == 100
    assert job_cost(data, "f") == 0


def test_discount_in_advance():
    message, discounted_total = discount_in_advance(data, "a", True)
    assert message == "Your amount to pay with discount is: $125.00"
    assert discounted_total == 125.0


    message, full_total = discount_in_advance(data, "a", False)
    assert message == "You have to pay full amount: $250.00"
    assert full_total == 250.0


    message, total = discount_in_advance(data, "f", True)
    assert message == "Invalid option"
    assert total == 0
