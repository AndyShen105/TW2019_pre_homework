# TW2019_pre_homework
# Function Description
## Input:
1. Size of road grid
2. Connectivity description of road grid


## Output:
a maze which descripted by string.

## TestCase:
Input:
```
3 3
0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1
```
Output:
```
[W] [W] [W] [W] [W] [W] [W]
[W] [R] [W] [R] [R] [R] [W]
[W] [R] [W] [R] [W] [R] [W]
[W] [R] [R] [R] [R] [R] [W]
[W] [W] [W] [R] [W] [R] [W]
[W] [R] [R] [R] [W] [R] [W]
[W] [W] [W] [W] [W] [W] [W]
```
*Notice: more details in problem description.*

# Development Environment
python 2.7.8

# File Manifest
```
tw_homework
│───README.md 
└───drawMaze.py      # 1. Rendering the maze to string; 2. Checking correctness of input.
└───unitTest.py      # Running some unit tests.
```
# Unit Test
Check the correctness of input:
## Invalid number format
the input contains non-numeric parameters.
## Number out of range
1. the number is negative.
2. the number is decimal.
3. x(y) of road grid is zero.
4. the x(y) of grid is out of range of maze.
## Incorrect command format 
1. invalid size of maze. eg "3 3 3" or "2"
2. the grid is incomplete, eg "1, 2,0;" or "1 2,0"
3. the grid pair is incomplete, eg "2,0;" or "2,0 ;"
## Maze format error
Difference value of x(y) between two grids is greater than one.
## Unit test for class maze
# How To Start
1. Running the main program
```shell
python drawMaze.py
```
TestCase:
> 3 3
0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1
    
2. Running unit tests.
```shell
python unitTest.py
```
