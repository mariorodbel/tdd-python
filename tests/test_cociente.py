from app.operaciones import cociente


class TestClass:
    def test_cociente(self):
        assert cociente(25, 5) == 5
        assert cociente(98, 6) == 16
        assert cociente(32, 4) == 8
        assert cociente(54, 3) == 18
