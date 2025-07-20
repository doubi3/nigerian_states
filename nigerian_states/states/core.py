import json
from pathlib import Path

class NigerianStates:
    def __init__(self):
        self.data = self._load_data()

    def _load_data(self):
        data_path = Path(__file__).parent / "data" / "states_lgas.json"
        try:
            with open(data_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            raise RuntimeError(f"Data file not found: {data_path}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Error decoding JSON: {e}")

    def get_states(self):
        """Return all Nigerian states."""
        return list(self.data.keys())

    def get_lgas(self, state):
        """Return LGAs for a given state (case-insensitive)."""
        # Normalize state name for case-insensitive matching
        state_map = {k.lower(): k for k in self.data.keys()}
        key = state_map.get(state.lower())
        if key:
            return self.data[key]
        return []

    def search_lga(self, query):
        """Search LGAs by name (case-insensitive)."""
        return [
            lga for lgas in self.data.values() 
            for lga in lgas 
            if query.lower() in lga.lower()
        ]
