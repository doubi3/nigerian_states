# Nigerian States and LGAs

A Python package for accessing Nigerian states and their respective Local Government Areas (LGAs).

## Features
- List all Nigerian states
- Get LGAs for a given state (case-insensitive)
- Search LGAs by name (case-insensitive)

## Usage
```python
from nigerian_states.states.core import NigerianStates

ng = NigerianStates()
print(ng.get_states())  # List all states
print(ng.get_lgas('Lagos'))  # List LGAs in Lagos
print(ng.search_lga('Ikeja'))  # Search for LGAs containing 'Ikeja'
```

## Installation
Clone the repo and install with pip:
```bash
pip install .
```

## License
MIT
