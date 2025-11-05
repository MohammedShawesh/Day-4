import math


class Character:
    def __init__(self, name: str, level: int = 1, power: int = 10):
        self.name = name
        self.level = level
        self.base_power = power
        self.max_health = 100 + (level - 1) * 10
        self.health = self.max_health
        self.power = self.base_power + (level - 1) * 5
        print(f"\nCreated {self.name} (Lvl {self.level}) enters the world of chronicles")


    def attack(self, target):
        if self.health <= 0:
            print(f"{self.name} is defeated and cannot attack.")
            return 0
        damage = self.power
        target.take_hit(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage.")
        return damage


    def take_hit(self, damage):
        if self.health <= 0:
            return 0

        self.health -= damage
        if self.health < 0:
            self.heaalth = 0
        if self.health == 0:
            print(f" {self.name} has been slain")
        return self.health


    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.power += 5
        self.health = self.max_health

        print(f"{self.name} leveled up to Lvl {self.level}!")
        print(f" stats: Power +5 ({self.power}), Max Health +10 ({self.max_health})")


    def get_status(self):
        status = (
            f"Status: {self.name}\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}/{self.max_health}\n"
            f"Power: {self.power}"
        )
        print(status)


class Warrior(Character):
    MAX_RAGE = 100
    RAGE_COST_SMASH = 50
    RAGE_GAIN_ATTACK = 15

    def __init__(self, name: str, level=1, power=12):
        super().__init__(name, level, power)
        self.rage = 0
        self.max_health += 5
        self.health = self.max_health

    def attack(self, target):
        if self.health <= 0:
            print(f"{self.name} is defeated and cannot attack.")
            return 0
        damage = self.power
        target.take_hit(damage)
        self.rage = min(self.MAX_RAGE, self.rage + self.RAGE_GAIN_ATTACK)

        print(f"{self.name} strikes {target.name} for {damage} damage and builds {self.RAGE_GAIN_ATTACK} rage.")

        return damage

    def power_smash(self, target):
        if self.rage < self.RAGE_COST_SMASH:
            print(f"{self.name} needs {self.RAGE_COST_SMASH - self.rage} more rage for Power Smash!")
            return 0

        if self.health <= 0:
            print(f"{self.name} is defeated and cannot Power Smash.")
            return 0
        self.rage -= self.RAGE_COST_SMASH
        damage = self.power * 2
        target.take_hit(damage)

        print(
            f"{self.name} UNLEASHES POWER SMASH on {target.name} for {damage} CRITICAL damage! Rage remaining: {self.rage}")

        return damage

    def get_status(self):
        super().get_status()
        print(f"Rage: {self.rage}/{self.MAX_RAGE}")


class Mage(Character):
    MANA_COST_SPELL = 30
    MANA_RESTORE_MEDITATE = 40

    def __init__(self, name: str, level=1, power=8):
        super().__init__(name, level, power)
        self.max_mana = 80 + (level - 1) * 20
        self.mana = self.max_mana

    def cast_spell(self, target):
        if self.mana < self.MANA_COST_SPELL:
            print(f"{self.name} failed to cast! Needs {self.MANA_COST_SPELL - self.mana} more mana.")
            return 0
        if self.health <= 0:
            print(f"{self.name} is defeated and cannot cast a spell.")
            return 0
        self.mana -= self.MANA_COST_SPELL
        damage = math.floor(self.power * 1.5)
        target.take_hit(damage)

        print(f"{self.name} CASTS FIREBALL on {target.name} for {damage} magical damage! Mana remaining: {self.mana}")
        return damage

    def meditate(self):
        if self.health <= 0:
            print(f"{self.name} is defeated and cannot meditate.")
            return 0
        mana_restored = self.MANA_RESTORE_MEDITATE
        self.mana = min(self.max_mana, self.mana + mana_restored)

        print(f"{self.name} meditates peacefully and restores {mana_restored} mana. Current mana: {self.mana}")
        return mana_restored

    def get_status(self):
        super().get_status()
        print(f"Mana: {self.mana}/{self.max_mana}")