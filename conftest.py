import pytest

from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture(scope="function")
def bun_exemplar():
    bun: Bun = Bun("black bun", 100)
    return bun


@pytest.fixture(scope="function")
def burger_exemplar():
    burger: Burger = Burger()
    return burger


@pytest.fixture(scope="function")
def database_exemplar():
    database: Database = Database()
    return database


@pytest.fixture(scope="function")
def ingredient_exemplar():
    ingredient: Ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    return ingredient


@pytest.fixture(scope="function")
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "black bun"
    mock_bun.get_price.return_value = 100
    return mock_bun


@pytest.fixture(scope="function")
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_sauce.get_name.return_value = "sour cream"
    mock_sauce.get_price.return_value = 200
    return mock_sauce


@pytest.fixture(scope="function")
def mock_filling():
    mock_filling = Mock()
    mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_filling.get_name.return_value = "sausage"
    mock_filling.get_price.return_value = 300
    return mock_filling


@pytest.fixture(scope="function")
def made_burger(burger_exemplar, mock_sauce, mock_filling, mock_bun):
    burger_exemplar.set_buns(mock_bun)
    burger_exemplar.add_ingredient(mock_sauce)
    burger_exemplar.add_ingredient(mock_filling)
