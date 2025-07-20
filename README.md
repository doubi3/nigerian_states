# Nigerian States and LGAs

A Python package for accessing Nigerian states and their respective Local Government Areas (LGAs).

## Features
- List all Nigerian states
- Get LGAs for a given state (case-insensitive)
- Search LGAs by name (case-insensitive)

## Installation

Install from PyPI (when available):
```bash
pip install nigerian-states
```

Or install from source:
```bash
git clone https://github.com/doubi3/nigerian-states.git
cd nigerian-states
pip install .
```

## Usage

```python
from nigerian_states.states.core import NigerianStates

ng = NigerianStates()

# List all states
states = ng.get_states()
print(states)

# Get LGAs for a state
lagos_lgas = ng.get_lgas('Lagos')
print(lagos_lgas)

# Search for LGAs containing a substring
search_results = ng.search_lga('Ikeja')
print(search_results)
```

## API Reference

### class NigerianStates

#### get_states()
> Returns a list of all Nigerian state names.

#### get_lgas(state)
> Returns a list of LGAs for the given state (case-insensitive). Returns an empty list if the state is not found.

#### search_lga(query)
> Returns a list of LGAs whose names contain the query substring (case-insensitive).

## Contributing

Contributions, bug reports, and feature requests are welcome! Please open an issue or submit a pull request on GitHub.

## License

MIT License. See [LICENSE](LICENSE) for details.

## Author

Mark Ekperi

For questions or suggestions, please contact [Mark Ekperi](mailto:mark.ekperi@gmail.com).
