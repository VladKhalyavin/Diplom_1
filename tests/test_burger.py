import pytest


class TestBurger:

    def test_get_receipt_3_ingredients_successful_getting_receipt(self, burger_exemplar, made_burger):
        """Проверка рецепта и цены бургера из 3 ингредиентов \n Метод Burger.get_receipt"""
        assert burger_exemplar.get_receipt() == ('(==== black bun ====)\n'
                                                 '= sauce sour cream =\n'
                                                 '= filling sausage =\n'
                                                 '(==== black bun ====)\n'
                                                 '\n'
                                                 'Price: 700')

    @pytest.mark.parametrize('index, new_index, result', [(0, 1, "sausage"), (0, 0, "sour cream")])
    def test_move_ingredient_successful_moving(self, burger_exemplar, made_burger, index, new_index, result):
        """Проверка перемещения ингредиентов \n Метод Burger.move_ingredient"""
        burger_exemplar.move_ingredient(index, new_index)

        assert len(burger_exemplar.ingredients) == 2 and burger_exemplar.ingredients[0].get_name() == result

    def test_remove_ingredient_successful_moving(self, burger_exemplar, made_burger):
        """
        Проверка перемещения ингредиентов \n Метод Burger.remove_ingredient
        Добавлены два ингредиента (sour cream и sausage)
        После удаление в списке один игредиент - sausage
        """
        burger_exemplar.remove_ingredient(0)

        assert len(burger_exemplar.ingredients) == 1 and burger_exemplar.ingredients[0].get_name() == "sausage"
