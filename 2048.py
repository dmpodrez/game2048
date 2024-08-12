import random

def create_grid():
    return [[0] * 4 for _ in range(4)]

def add_new_tile(grid):
    empty_cells = [(r, c) for r in range(4) for c in range(4) if grid[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        grid[r][c] = 2 if random.random() < 0.9 else 4

def print_grid(grid):
    for row in grid:
        print("\t".join(map(str, row)))
    print()

# Создаем сетку 4x4
grid = create_grid()

# Добавляем две случайные плитки
add_new_tile(grid)
add_new_tile(grid)

# Выводим начальную сетку
print_grid(grid)
