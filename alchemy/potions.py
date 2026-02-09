#!/usr/bin/env
from alchemy.elements import (
    create_water, create_air, create_earth, create_fire
    )


def healing_potion():
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion():
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion():
    return (
        f"Invisibility potion brewed with {create_air()} and {create_water()}"
        )


def wisdom_potion():
    results = (
        f"{create_air()}, {create_earth()}, "
        f"{create_fire()} and {create_water()}"
    )
    return f"Wisdom potion brewed with all elements: {results}"
