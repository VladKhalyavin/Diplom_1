class TestBun:

    def test_get_name_black_bun_successful_getting_a_name(self, bun_exemplar):
        """Проверка получения имени булки \n Метод Bun.get_name"""
        assert bun_exemplar.get_name() == 'black bun'

    def test_get_price_100_successful_getting_a_price(self, bun_exemplar):
        """Проверка получения цены булки \n Метод Bun.get_price"""
        assert bun_exemplar.get_price() == 100
