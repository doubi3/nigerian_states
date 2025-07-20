
from nigerian_states.states.core import NigerianStates

def main():
    ng = NigerianStates()
    print("States:", ng.get_states())
    print("LGAs in Lagos:", ng.get_lgas('Lagos'))
    print("Search 'Ikeja':", ng.search_lga('Ikeja'))

if __name__ == "__main__":
    main()
