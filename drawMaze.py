# Create by AndyShen on 27.7.2018
# encoding: utf-8


class InputException(Exception):

    def __init__(self, error_index):
        error_list = ['Invalid number format ​.',
                      'Number out of range ​.',
                      'Incorrect command format ​.',
                      'Maze format error.']
        self.error = error_list[error_index]


def is_non_number(para):
    """
    check if the para is alphabet.
    :param para: string
    :return: true or false
    """
    try:
        float(para)
    except ValueError:
        return False
    return True


def is_positive_integer(para):
    """
    check if the para is positive integer.
    :param para: string
    :return: true or false
    """
    number = float(para)
    if (number < 0.0) or (len(para.split('.')) != 1):
        return False
    return True


def check_input_correctness(road_grid_str, render_grid_str):
    """
    check the correctness of input:
        1. 'Invalid number format ​.'
            a. the input contains non-numeric parameters.
        2. 'Number out of range ​.'
            a. the number is negative.
            b. the number is decimal.
            c. x(y) of road grid is zero.
            d. the x(y) of grid is out of range of maze.
        3. 'Incorrect command format ​.'
            a. invalid size of maze. eg "3 3 3" or "2"
            b. the grid is incomplete, eg "1, 2,0;" or "1 2,0"
            c. the grid pair is incomplete, eg "2,0;" or "2,0 ;"
        4. 'Maze format error.'
            a. Difference value of x(y) between two grids is greater than one.

    :param road_grid_str: string
    :param render_grid_str: string
    :return: 0 -> Invalid number format
             1 -> Number out of range
             2 -> Incorrect command format
             3 -> Maze format error
             True -> the input is normal.
    """
    road_grid_list = road_grid_str.split(' ')

    # invalid size of maze. eg "3 3 3" or "2".
    if len(road_grid_list) != 2:
        return 2
    for para in road_grid_list:

        # the input contains non-numeric parameters.
        if not is_non_number(para):
            return 0

        # the number is negative or decimal or x(y) of road grid is zero.
        if not is_positive_integer(para) or int(para) == 0:
            return 1
    x_max = int(road_grid_list[0])
    y_max = int(road_grid_list[1])

    render_grid_list = render_grid_str.split(';')
    for grid_pair_str in render_grid_list:
        grid_pair = grid_pair_str.split(' ')

        # the grid pair is incomplete, eg "2,0;" or "2,0 ;".
        if len(grid_pair) != 2 or grid_pair[0] == '' or grid_pair[1] == '':
            return 2
        temp_list = []
        for grid_str in grid_pair:
            grid = grid_str.split(',')

            # the grid is incomplete, eg "1, 2,0;" or "1 2,0".
            if len(grid) != 2 or grid[0] == '' or grid[1] == '':
                return 2

            # the input contains non-numeric parameters.
            if (not is_non_number(grid[0])) or (not is_non_number(grid[1])):
                return 0

            x = int(grid[0])
            y = int(grid[1])

            # the number is negative or decimal.
            if (not is_positive_integer(grid[0])) or (not is_positive_integer(grid[1])) or x >= x_max or y >= y_max:
                return 1
            temp_list.append(x)
            temp_list.append(y)

        # Difference value of x(y) between two grids is greater than one.
        if not ((temp_list[0] == temp_list[2] and abs(temp_list[1] - temp_list[3]) == 1) or \
                (abs(temp_list[0] - temp_list[2]) == 1 and temp_list[1] == temp_list[3])):
            return 3
    return True


class Maze:
    """
    Class maze: a class holding the information of a maze which can transform the input to a mazeText.
    Attributes:
        x_max: width of maze, int
        y_max: depth of maze, int
        road_map: road information of maze, list[][]
        render_grid_str: connectedness fo grids, string
    """

    def __init__(self, road_grid_str, render_grid_str):
        road_grid_list = road_grid_str.split(' ')
        self.x_max = int(road_grid_list[0]) * 2 + 1
        self.y_max = int(road_grid_list[1]) * 2 + 1
        self.road_map = self.init_road_map()
        self.render_grid_str = render_grid_str

    def init_road_map(self):
        """
        init a list to record the maze
        :return: list[[]]
        """
        road_map = [([0] * self.y_max) for i in range(self.x_max)]
        x_index = 1
        while x_index < self.x_max:
            y_index = 1
            while y_index < self.y_max:
                road_map[x_index][y_index] = 1
                y_index += 2
            x_index += 2
        return road_map

    def create_maze(self):
        """
        create a maze by connectedness fo grids
        :return:
        """
        render_grid_list = self.render_grid_str.split(';')
        for para in render_grid_list:
            p_1 = para.split(' ')[0]
            x_1 = int(p_1.split(',')[0]) * 2 + 1
            y_1 = int(p_1.split(',')[1]) * 2 + 1

            p_2 = para.split(' ')[1]
            x_2 = int(p_2.split(',')[0]) * 2 + 1
            y_2 = int(p_2.split(',')[1]) * 2 + 1

            x_t = (x_1 + x_2) / 2
            y_t = (y_1 + y_2) / 2
            self.road_map[x_t][y_t] = 1

    def render_maze(self):
        """
        transform maze to string
        :return:
        """
        maze_text = ''
        for x_index in range(self.x_max):
            for y_index in range(self.y_max):
                if self.road_map[x_index][y_index] == 1:
                    maze_text += '[r] '
                else:
                    if y_index == self.y_max - 1:
                        maze_text += '[w]' + '\n'
                    else:
                        maze_text += '[w] '
        return maze_text


def main():
    # get the input
    road_grid_str = raw_input()
    render_grid_str = raw_input()

    # check if it is correct of input
    try:
        flag = check_input_correctness(road_grid_str, render_grid_str)
        if not flag:
            raise (InputException(flag))
    except InputException, x:
        print x.error
    else:
        maze = Maze(road_grid_str, render_grid_str)
        maze.create_maze()
        maze_text = maze.render_maze()
        print(maze_text)


if __name__ == "__main__":
    main()

