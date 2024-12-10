import pytest
from project import table_of_information, job_cost, discount_in_advance


def test_table_of_information(data):
    output = table_of_information(data)
    expected_output = [
        "a: Full Mouth Restoration, 250",
        "b: Dental Implants, 50",
        "c: Teeth Whitening, 100",
        "d: General Dentistry, 150",
        "e: Crown and Bridgework, 75",
    ]
    assert output == expected_output


def test_job_cost(data):
    selected_job = "a"
    work, cost = data[selected_job]
    assert work == "Full Mouth Restoration"
    assert cost == 250

    invalid_job = "f"
    assert invalid_job not in data


def test_discount_in_advance(data):
    selected_job = "a"
    work, cost = data[selected_job]
    advance_payment = True
    discount_total = cost * 0.5 if advance_payment else cost
    assert discount_total == 125.0

    advance_payment = False
    full_total = cost * 0.5 if advance_payment else cost
    assert full_total == 250.0
