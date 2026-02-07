#!/usr/bin/env
import alchemy


def ft_sacred_scroll():
    print("=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print(
        f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}"
        )
    print(
        f"alchemy.elements.create_water(): {alchemy.elements.create_water()}"
        )
    print(
        f"alchemy.elements.create_earth(): {alchemy.elements.create_earth()}"
        )
    print(
        f"alchemy.elements.create_air(): {alchemy.elements.create_air()}"
        )

    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.water(): {alchemy.create_water()}")

    try:
        alchemy.create_earth()
    except AttributeError as e:
        print(f"alchemy.create_earth(): {e}")
    try:
        alchemy.create_air()
    except AttributeError as e:
        print(f"alchemy.create_air(): {e}")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    ft_sacred_scroll()
