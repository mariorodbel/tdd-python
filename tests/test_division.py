from app.operaciones import division


class TestClass:
    def test_division(self):
        assert division(6, 2) == 3
        assert division(10, 2) == 5
        assert division(5, 5) == 1
        assert division(13, 13) == 1
