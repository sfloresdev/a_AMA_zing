import os
from utils.maze.maze_engine import MazeGenerator
from utils.parser.config_parser import MazeConfig


class MazeVisualizer:
    def __init__(self, maze_data: list[list]) -> None:
        self.maze = maze_data
        self.show_path = False
        self.wall_color = "\033[1;37m"
        self.reset_color = "\033[0m"
        self.colors = {
            "red": "\033[0;31m",
            "green": "\033[0;32m",
            "blue": "\033[0;34m",
            "yellow": "\033[0;33m",
            "white": "\033[1;37m"
        }

    def update_data(self, new_maze_data: list[list]) -> None:
        """Nos permite actualizar el laberinto sin crear un nuevo objeto"""
        self.maze = new_maze_data

    def draw(self, path_coords=None) -> None:
        if path_coords is None:
            path_coords = set()

        os.system('cls' if os.name == 'nt' else 'clear')

        for r, row in enumerate(self.maze):
            line = ""
            for c, cell in enumerate(row):
                # 1. Prioridad: Mostrar el camino (Solution Path)
                if self.show_path and (r, c) in path_coords:
                    line += "\033[0;33m.\033[0m"
                
                # 2. Paredes
                elif cell == 1:
                    # Lógica de conexión de líneas
                    if r % 2 == 0:
                        if c % 2 == 0:
                            line += f"{self.wall_color}╋━{self.reset_color}"
                        else:
                            line += f"{self.wall_color}━━{self.reset_color}"
                    else:
                        if c % 2 == 0:
                            line += f"{self.wall_color}┃ {self.reset_color}"
                        else:
                            line += "  " # Esto no debería pasar si la matriz es 2n+1

                # 3. Entrada
                elif cell == 'E':
                    line += "\033[45m  \033[0m"

                # 4. Salida
                elif cell == 'S':
                    line += "\033[41m  \033[0m"

                # 5. Pasillos vacíos
                else:
                    line += "  "  # IMPORTANTE: Espacio para que no se deforme
            print(line)

    def change_color(self, color_name: str) -> None:
        if color_name in self.colors:
            self.wall_color = self.colors[color_name]

    def create_42_logo(self):
        pass
