from app.rot_cipher import rot13


class TestClass:
    def test_rot13_cipher(self):
        assert rot13("buenastardes") == "ohranfgneqrf"
        assert rot13("pelota") == "crybgn"
        assert rot13("holamundo!") == "ubynzhaqb!"
        assert rot13("melomano") == "zrybznab"
