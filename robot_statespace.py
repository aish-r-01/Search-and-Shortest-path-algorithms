
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1]
]

class RobotState:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
    
    def is_valid(self):
        if self.x < 0 or self.x >= len(maze[0]) or self.y < 0 or self.y >= len(maze):
            return False
        if maze[self.y][self.x] == 1:
            return False
        return True
    
    def get_next_states(self):
        next_states = []
        directions = ['north', 'east', 'south', 'west']
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        current_index = directions.index(self.direction)
        for i in [-1, 0, 1]:
            new_index = (current_index + i) % 4
            new_x = self.x + dx[new_index]
            new_y = self.y + dy[new_index]
            new_direction = directions[new_index]
            next_state = RobotState(new_x, new_y, new_direction)
            if next_state.is_valid():
                next_states.append(next_state)
        return next_states

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        
    def solve(self):
        start_state = RobotState(len(maze[0])//2, len(maze)//2, 'north')
        frontier = [start_state]
        explored = set()
        while frontier:
            state = frontier.pop(0)
            if (state.x, state.y, state.direction) in explored:
                continue
            explored.add((state.x, state.y, state.direction))
            if state.x == 0 or state.x == len(self.maze[0])-1 or state.y == 0 or state.y == len(self.maze)-1:
                return state
            frontier += state.get_next_states()
        return None


solver = MazeSolver(maze)
solution = solver.solve()
if solution:
    print("Found solution:", solution.x, solution.y, solution.direction)
else:
    print("No solution found.")
