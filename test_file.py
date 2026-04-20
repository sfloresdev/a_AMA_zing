def print_pretty_maze(grid) -> None:
    """
    Dibuja el laberinto en la terminal de forma visual.
    (Herramienta temporal para el equipo de algoritmos).
    """
    print("\n--- Vista Visual del Laberinto ---")

    for y, row in enumerate(grid):
        # 1. Dibujamos los "techos" (Paredes Norte) de toda la fila
        top_line = ""
        for cell in row:
            top_line += "+---" if cell.walls['N'] else "+   "
        top_line += "+"  # Esquina superior derecha del borde final
        print(top_line)

        # 2. Dibujamos los "pasillos" (Paredes Oeste) y el espacio interior
        mid_line = ""
        for x, cell in enumerate(row):
            mid_line += "|   " if cell.walls['W'] else "    "
            # Si es la última celda de la fila, cerramos con su pared Este
            if x == len(row) - 1:
                mid_line += "|" if cell.walls['E'] else " "
        print(mid_line)

        if y == len(grid) - 1:
            bottom_line = ""
            for cell in row:
                bottom_line += "+---" if cell.walls['S'] else "+   "
            bottom_line += "+"
            print(bottom_line)
