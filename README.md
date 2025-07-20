# Nigerian States and LGAs

A Python package for accessing Nigerian states and their respective Local Government Areas (LGAs).

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

```
pip install .
```

## License
MIT
