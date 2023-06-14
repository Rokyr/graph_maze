from pathlib import Path

from maze_solver.models.border import Border
from maze_solver.models.maze import Maze
from maze_solver.models.role import Role
from maze_solver.models.square import Square
from maze_solver.persistence.serialiser import dump_squares, load_squares

maze = Maze(
    squares=(
        Square(0, 0, 0, Border.TOP | Border.LEFT),
        Square(1, 0, 1, Border.TOP | Border.RIGHT),
        Square(2, 0, 2, Border.LEFT | Border.RIGHT, Role.EXIT),
        Square(3, 0, 3, Border.TOP | Border.LEFT | Border.RIGHT),
        Square(4, 1, 0, Border.BOTTOM | Border.LEFT | Border.RIGHT),
        Square(5, 1, 1, Border.LEFT | Border.RIGHT),
        Square(6, 1, 2, Border.BOTTOM | Border.LEFT),
        Square(7, 1, 3, Border.RIGHT),
        Square(8, 2, 0, Border.TOP | Border.LEFT, Role.ENTRANCE),
        Square(9, 2, 1, Border.BOTTOM),
        Square(10, 2, 2, Border.TOP | Border.BOTTOM),
        Square(11, 2, 3, Border.BOTTOM | Border.RIGHT),
    )
)


def mazes_path():
    directory_path = Path("C:/Users/FiercePC/PycharmProjects/pythonProject1/maze-solver/mazes")
    return directory_path


path = mazes_path()/"miniature.maze"
dump_squares(width=4, height=3, squares=maze.squares, path=path)