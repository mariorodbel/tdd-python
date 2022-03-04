from app.operaciones import multiplicacion


class TestClass:
    def test_multiplicacion(self):
        assert multiplicacion(1, 2) == 2
        assert multiplicacion(5, 2) == 10
        assert multiplicacion(5, 5) == 25
        assert multiplicacion(11, 13) == 143
