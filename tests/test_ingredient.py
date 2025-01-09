from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:

    def test_get_price_100_successful_getting_a_price(self, ingredient_exemplar):
        """Проверка получения цены ингредиента \n Метод Ingredient.get_price"""
        assert ingredient_exemplar.get_price() == 100

    def test_get_name_hot_sauce_successful_getting_a_name(self, ingredient_exemplar):
        """Проверка получения имени ингредиента \n Метод Ingredient.get_name"""
        assert ingredient_exemplar.get_name() == 'hot sauce'

    def test_get_type_sauce_successful_getting_a_type(self, ingredient_exemplar):
        """Проверка получения имени ингредиента \n Метод Ingredient.get_type"""
        assert ingredient_exemplar.get_type() == INGREDIENT_TYPE_SAUCE
