import unittest
from nigerian_states.states.core import NigerianStates

class TestNigeriaGeo(unittest.TestCase):
    def setUp(self):
        self.geo = NigerianStates()

    def test_get_states(self):
        states = self.geo.get_states()
        self.assertIn("Lagos", states)

    def test_get_lgas(self):
        lgas = self.geo.get_lgas("Lagos")
        self.assertIn("Ikeja", lgas)

if __name__ == "__main__":
    unittest.main()