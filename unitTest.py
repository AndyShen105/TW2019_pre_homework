  # create by AndyShen on 27.7.2018
# -*- coding: UTF-8 -*-
import unittest
from drawMaze import *


class DrawMazeTest(unittest.TestCase):

    def test_invalid_number_format(self):
        road_grid_str = '3 3'
        render_grid_str = '0,b 0,;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1'
        flag = check_input_correctness(road_grid_str, render_grid_str)
        self.assertEqual(flag, 0)

        road_grid_str = '3 #'
        render_grid_str = '0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1'
        flag = check_input_correctness(road_grid_str, render_grid_str)
        self.assertEqual(flag, 0)

    def test_number_out_of_range(self):
        road_grid_str = '3 -3'
        render_grid_str = '0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1'
        flag = check_input_correctness(road_grid_str, render_grid_str)
        self.assertEqual(flag, 1)

        road_grid_str = '3 0.1'
        render_grid_str = '0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1'
        flag = check_input_correctness(road_grid_str, render_grid_str)
        self.assertEqual(flag, 1)

        road_grid_str = '3 0'
        render_grid_str = '0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1'
        flag = check_input_correctness(road_grid_str, render_grid_str)
        self.assertEqual(flag, 1)

    def test_incorrect_command_format(self):
        road_grid_str = '3 3 6'
        render_grid_str = '0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1'
        flag = check_input_correctness(road_grid_str, render_grid_str)
        self.assertEqual(flag, 2)

        road_grid_str = '3 3'
        render_grid_str = '0,1 0,;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1'
        flag = check_input_correctness(road_grid_str, render_grid_str)
        self.assertEqual(flag, 2)

        road_grid_str = '3 3'
        render_grid_str = '0,1 ;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1'
        flag = check_input_correctness(road_grid_str, render_grid_str)
        self.assertEqual(flag, 2)

        road_grid_str = '3 3'
        render_grid_str = '0,1 0;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1'
        flag = check_input_correctness(road_grid_str, render_grid_str)
        self.assertEqual(flag, 2)

        road_grid_str = '3 3'
        render_grid_str = '0,1;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1'
        flag = check_input_correctness(road_grid_str, render_grid_str)
        self.assertEqual(flag, 2)

    def test_maze_format_error(self):
        road_grid_str = '3 3'
        render_grid_str = '0,1 0,2;0,0 2,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1'
        flag = check_input_correctness(road_grid_str, render_grid_str)
        self.assertEqual(flag, 3)

    def test_maze(self):
        road_grid_str = '3 3'
        render_grid_str = '0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1'
        maze = Maze(road_grid_str, render_grid_str)
        maze.create_maze()
        maze_text = maze.render_maze()

        self.assertEqual(maze_text, '''[w] [w] [w] [w] [w] [w] [w]
[w] [r] [w] [r] [r] [r] [w]
[w] [r] [w] [r] [w] [r] [w]
[w] [r] [r] [r] [r] [r] [w]
[w] [w] [w] [r] [w] [r] [w]
[w] [r] [r] [r] [w] [r] [w]
[w] [w] [w] [w] [w] [w] [w]
''')


if __name__ == '__main__':
    unittest.main()
