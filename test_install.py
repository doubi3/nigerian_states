
from nigerian_states.states.core import NigerianStates

def main():
    ng = NigerianStates()
    print("States:", ng.get_states())
    print("LGAs in Bayelsa:", ng.get_lgas('Bayelsa'))
    print("Search 'Yenagoa':", ng.search_lga('Yenagoa'))

if __name__ == "__main__":
    main()
