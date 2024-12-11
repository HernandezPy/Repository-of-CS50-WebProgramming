import pytest
from tabulate import tabulate
from Project import table_of_information, job_cost, discount_in_advance

data = {

    "a": ("Full Mouth Restoration", 250),
    "b": ("Dental Implants", 50),
    "c": ("Teeth Whitening", 100),
    "d": ("General Dentistry", 150),
    "e": ("Crown and Bridgework", 75),
}

table_of_information(data)
discount_in_advance(data)


def test_table_of_information(capsys):
    table_of_information(data)
    capture = capsys.readouterr()
    table = [[key.upper(), work, f"${cost}"] for key, (work, cost) in data.items()]
    headers = ["Options", "Service", "Cost"]
    expected_output = tabulate(table, headers, tablefmt="grid") + "\n"
    assert capture.out == expected_output


def test_job_cost(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "a")
    assert job_cost(data) == 250
    monkeypatch.setattr("builtins.input", lambda _: "b")
    assert job_cost(data) == 50
    monkeypatch.setattr("builtins.input", lambda _: "z")
    assert job_cost(data) == 0


def test_discount_in_advance(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "yes")
    discount_in_advance(150)
    capture = capsys.readouterr()
    assert "Your amount to pay with discount is: $75.00" in capture.out
    monkeypatch.setattr("builtins.input", lambda _: "no")
    discount_in_advance(150)
    capture = capsys.readouterr()
    assert "You have to pay full amount: $150.00" in capture.out
