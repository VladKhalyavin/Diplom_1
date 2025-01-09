from typing import List, Tuple
from data import DATASET_INGREDIENTS, DATASET_BUNS


class TestDatabase:

    def test_get_available_buns_successful_getting_buns(self, database_exemplar):
        """Проверка получения списка доступных булок \n Метод Database.available_buns"""
        buns_list: List[Tuple] = []
        buns = database_exemplar.available_buns()
        for bun in buns:
            buns_list.append((bun.get_name(), bun.get_price()))

        assert buns_list == DATASET_BUNS

    def test_get_available_ingredients_successful_getting_buns(self, database_exemplar):
        """Проверка получения списка доступных булок \n Метод Database.available_ingredients"""
        ingredients_list: List[Tuple] = []
        ingredients = database_exemplar.available_ingredients()
        for ingredient in ingredients:
            ingredients_list.append((ingredient.get_type(), ingredient.get_name(), ingredient.get_price()))

        assert ingredients_list == DATASET_INGREDIENTS
