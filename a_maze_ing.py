
import sys
from utils.parser.config_parser import MazeConfig


def main() -> None:

    if len(sys.argv) != 2:
        print("Use: python3 a_maze_ing.py config.txt")
        sys.exit(1)

    print("Test function")
    config_file: str = sys.argv[1]

    try:
        config = MazeConfig(config_file)

        print("Prueba de carga de configuracion")
        print(f"{config.width}")
        print(f"{config.height}")
        print(f"{config.entry}")
        print(f"{config.exit}")
        print(f"{config.outputfile}")
        print(f"{config.perfect}")

    except (FileNotFoundError, ValueError) as e:
        print(f"{e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error -> {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
