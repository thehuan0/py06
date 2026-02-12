import alchemy.transmutation.basic
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life


def ft_pathway_debate() -> None:
    print("\n=== Pathway Debate Mastery ===\n")
    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {alchemy.transmutation.lead_to_gold()}")
    print(f"stone_to_gem(): {alchemy.transmutation.stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")

    print("\nTesting Package Access:")
    print(f"alchemy.transmutation.lead_to_gold():"
          f" {alchemy.transmutation.lead_to_gold()}")
    print(f"alchemy.transmutation.philosophers_stone():"
          f" {alchemy.transmutation.philosophers_stone()}")
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    ft_pathway_debate()
