from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone():
    info = "Philosopher’s stone created using "
    return (f"{info}{lead_to_gold()} and {healing_potion()}")


def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
