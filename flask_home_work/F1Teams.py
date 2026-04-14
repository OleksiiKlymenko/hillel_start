import random

class F1Team:
    def __init__(self, name, driver, best_position, price):
        self.name = name
        self.driver = driver
        self.best_position = best_position
        self.price = price

    def __str__(self):
        # Повертає гарний рядок при виклику print()
        return f"Команда: {self.name} | Пілот: {self.driver} | Найкраща позиція в сезоні: {self.best_position} | Ціна: {self.price}$"


def generate_teams():
    teams = []

    f1_data = [
        ("Oracle Red Bull Racing", "Max Verstappen", "Liam Lawson", 50),
        ("Mercedes-AMG Petronas", "George Russell", "Andrea Kimi Antonelli", 45),
        ("Scuderia Ferrari", "Lewis Hamilton", "Charles Leclerc", 48),
        ("McLaren Formula 1 Team", "Lando Norris", "Oscar Piastri", 42),
        ("Aston Martin Aramco", "Fernando Alonso", "Lance Stroll", 35),
        ("Alpine F1 Team", "Pierre Gasly", "Jack Doohan", 25),
        ("Williams Racing", "Alexander Albon", "Carlos Sainz", 28),
        ("Haas F1 Team", "Oliver Bearman", "Esteban Ocon", 20),
        ("Audi F1 Team", "Nico Hülkenberg", "Gabriel Bortoleto", 38),
        ("Visa Cash App RB", "Yuki Tsunoda", "Isack Hadjar", 22),
        ("Cadillac Andretti F1", "Sergio Perez", "Alex Palou", 30)
    ]

    for team_name, driver1, driver2, price_base in f1_data:
        teams.append(F1Team(team_name, driver1, 1, price_base * 1000000))
        teams.append(F1Team(team_name, driver2, 2, (price_base - 5) * 1000000))

    return teams

##for team in generate_teams():
##    print(team)