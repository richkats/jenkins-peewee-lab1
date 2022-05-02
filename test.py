import pytest
import main
import os.path


def test_create_database():
    main.init()
    assert os.path.exists(main.db_file) == True


def test_clients_fields():
    assert main.Clients.name == True
    assert main.Clients.city == True
    assert main.Clients.address == True


def test_orders_fields():
    assert main.Orders.client == True
    assert main.Orders.amount == True
    assert main.Orders.date == True
    assert main.Orders.description == True


def test_clients_len():
    main.fill()
    assert len(main.Clients.select()) >= 10


def test_orders_len():
    main.fill()
    assert len(main.Orders.select()) >= 10