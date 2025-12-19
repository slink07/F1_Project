from providers.live_provider import LiveProvider
from data.classification import get_classification

def main():
    provider = LiveProvider(2024, "Bharain", "R")
    provider.load()

    drivers = provider.get_drivers()
    laps = provider.get_laps()
    position = provider.get_Positions()


    print("Pilotos:", drivers)
    print("Voltas:",laps)
    print("Posições:",position)
    
    

    classification = get_classification(provider)
    print(classification)


if __name__ == "__main__":
    main()