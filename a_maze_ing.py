
import sys
from utils.parser.config_parser import MazeConfig
from utils.maze.maze_engine import MazeGenerator
from test_file import print_pretty_maze


def print_console(grid) -> None:
    print("\n----Test View----")
    for row in grid:
        line = "".join(cell.to_hex() for cell in row)
        print(line)
    print("-------------------")


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

        print("\nPrueba de visualizacion laberinto")
        generator = MazeGenerator(config)
        generator.generate_maze()

        grid = generator.get_grid()
        print_console(grid)
        print("----------------------------------\n")
        print("----------------------------------")
        print_pretty_maze(grid)

    except (FileNotFoundError, ValueError) as e:
        print(f"{e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected Error -> {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
