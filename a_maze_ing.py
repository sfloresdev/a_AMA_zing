
import sys
from utils.parser.config_parser import MazeConfig
from utils.maze.maze_engine import MazeGenerator
from utils.maze.maze_visualizer import MazeVisualizer
from utils.maze.gen_output_file import export_maze
from utils.algo.bfs import MazeSolver
#  from test_file import print_pretty_maze


def main() -> None:
    if len(sys.argv) != 2:
        print("Use: python3 a_maze_ing.py config.txt")
        sys.exit(1)

    config_file = sys.argv[1]

    try:
        # 1. Cargar configuración
        config = MazeConfig(config_file)

        # 2. Generar el laberinto (Lógica)
        generator = MazeGenerator(config)
        generator.generate_maze()
        grid = generator.get_grid()
        solver = MazeSolver(grid, config.entry, config.exit)
        solved_path = solver.solve()

        export_maze(
            config.outputfile,
            grid,
            config.entry,
            config.exit,
            solved_path
        )

        # 3. Traducir y Visualizar (Estética)
        # Obtenemos la matriz de bloques (1s y 0s)
        matrix = generator.get_display_matrix()

        # Creamos el visualizador y dibujamos
        visualizer = MazeVisualizer(matrix)

        while True:
            visualizer.draw()
            print("\n=== A-Maze-Ing ===")
            print("1. Re-generate a new maze")
            print("2. Show/Hide path")
            print("3. Change colors")
            print("4. Quit")

            choice = input("\nChoice? (1-4): ")

            if choice == "1":
                # Aqui vendra backtracking recursivo
                gen = MazeGenerator(config)
                gen.generate_maze()
                visualizer.update_data(gen.get_display_matrix())

            elif choice == "2":
                visualizer.show_path = not visualizer.show_path

            elif choice == "3":
                new_color = input(
                    "Color (red/green/blue/yellow/white): ").lower()
                visualizer.change_color(new_color)

            elif choice == "4":
                break

        print(f"\nLaberinto de {config.width}x{config.height} generado.")
        print(f"Perfecto: {config.perfect} "
              f"| Entrada: {config.entry} |"
              f" Salida: {config.exit}"
              )

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
