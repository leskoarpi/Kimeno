import random


class Warrior:
    def __init__(self, name, hp, attack_power):
        try:
            self.name = name
            self.hp = hp
            self.attack_power = attack_power
            self.defense_mode = False
        except Exception as hiba:
            print(f"Hiba történt a harcos konstruktalasakor {hiba}")
    
    def attack(self, other_warrior):
        if not other_warrior.is_alive():
            print(f"{other_warrior.name} már nem él!")
            return
        
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        if other_warrior.defense_mode:
            damage = max(0, damage // 2)
            other_warrior.defense_mode = False

        if random.random() < 0.1:
            kritikusVagyVedekezes = random.choice(["crit", "defense"])
            if kritikusVagyVedekezes == "crit":
                print(f"{self.name} kritikus odaverést mért!")
                damage *= 2
            else:
                print(f"{self.name} cast: nuh uh")
                self.defense_mode = True

        other_warrior.hp -= damage
        print(f"{self.name} {damage} sebzést okozott {other_warrior.name}-nek.")

    def is_alive(self):
        return self.hp > 0


def battle(warrior1, warrior2):
    korok_szama = 0
    while warrior1.is_alive() and warrior2.is_alive():
        korok_szama += 1
        print(f"\n--- {korok_szama}. kör ---")
        
        # Harcos 1 támad
        warrior1.attack(warrior2)
        if warrior2.is_alive():
            print(f"{warrior2.name} életereje: {warrior2.hp}")
        else:
            print(f"{warrior2.name} elesett! {warrior1.name} nyert {korok_szama} kör után!")
            break
        
        # Harcos 2 támad, ha még él
        warrior2.attack(warrior1)
        if warrior1.is_alive():
            print(f"{warrior1.name} életereje: {warrior1.hp}")
        else:
            print(f"{warrior1.name} elesett! {warrior2.name} nyert {korok_szama} kör után!")
            break

try:
    warrior1 = Warrior("cigany", 100, 20)
    warrior2 = Warrior("magyar", 100, 18)
except Exception as e:
    print(f"Hiba történt a harcosok létrehozásakor: {e}")

battle(warrior1, warrior2)
