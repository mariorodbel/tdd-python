from app.operaciones import resto


class TestClass:
    def test_resto(self):
        assert resto(20, 3) == 2
        assert resto(30, 2) == 0
        assert resto(47, 2) == 1
        assert resto(7, 5) == 2
