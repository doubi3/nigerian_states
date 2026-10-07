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

    def test_state_and_lga_dataset_completeness(self):
        expected_counts = {
            "Abia": 17,
            "Adamawa": 21,
            "Akwa Ibom": 31,
            "Anambra": 21,
            "Bauchi": 20,
            "Bayelsa": 8,
            "Benue": 23,
            "Borno": 27,
            "Cross River": 18,
            "Delta": 25,
            "Ebonyi": 13,
            "Edo": 18,
            "Ekiti": 16,
            "Enugu": 17,
            "FCT": 6,
            "Gombe": 11,
            "Imo": 27,
            "Jigawa": 27,
            "Kaduna": 23,
            "Kano": 44,
            "Katsina": 34,
            "Kebbi": 21,
            "Kogi": 21,
            "Kwara": 16,
            "Lagos": 20,
            "Nasarawa": 13,
            "Niger": 25,
            "Ogun": 20,
            "Ondo": 18,
            "Osun": 30,
            "Oyo": 33,
            "Plateau": 17,
            "Rivers": 23,
            "Sokoto": 23,
            "Taraba": 16,
            "Yobe": 17,
            "Zamfara": 14,
        }
        self.assertEqual(
            {state: len(lgas) for state, lgas in self.geo.data.items()},
            expected_counts,
        )
        self.assertEqual(sum(expected_counts.values()), 774)
        for state, lgas in self.geo.data.items():
            with self.subTest(state=state):
                self.assertEqual(len(lgas), len(set(lgas)))
                self.assertTrue(all(lga == lga.strip() for lga in lgas))

    def test_edo_lga_list(self):
        self.assertEqual(
            self.geo.get_lgas("Edo"),
            [
                "Akoko-Edo",
                "Egor",
                "Esan Central",
                "Esan North-East",
                "Esan South-East",
                "Esan West",
                "Etsako Central",
                "Etsako East",
                "Etsako West",
                "Igueben",
                "Ikpoba-Okha",
                "Oredo",
                "Orhionmwon",
                "Ovia North-East",
                "Ovia South-West",
                "Owan East",
                "Owan West",
                "Uhunmwonde",
            ],
        )

if __name__ == "__main__":
    unittest.main()