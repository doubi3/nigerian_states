import unittest
from states.core import NigeriaGeo

class TestNigeriaGeo(unittest.TestCase):
    def setUp(self):
        self.geo = NigeriaGeo()

    def test_get_states(self):
        states = self.geo.get_states()
        self.assertIn("Lagos", states)

    def test_get_lgas(self):
        lgas = self.geo.get_lgas("Lagos")
        self.assertIn("Ikeja", lgas)

if __name__ == "__main__":
    unittest.main()