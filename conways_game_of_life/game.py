import random, copy

class Game():

    def __init__(self, height=20, width=60):
        """Creates a Game object for the driver class."""
        self.HEIGHT = height
        self.WIDTH = width
        self.next_cells = []
    
    def make_matrix(self):
        """Creates the matrix for the game."""
        # Create a list of list for the cells.
        self.next_cells = []
        for i in range(self.WIDTH):
            column = [] # Create a column.
            for j in range(self.HEIGHT):
                if random.randint(0,1) == 0:
                    column.append('#') # Add a living cell.
                else:
                    column.append(' ') # Add a dead cell.
            self.next_cells.append(column) # next_cells is a list of column lists.

    def calculate_steps(self):
        """Calculates the next step in Conway's game."""
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                # Get neighbouring cells coordinates.
                # `% WIDTH` ensures left_coord is always 
                # between 0 and WIDTH - 1
                left_coord = (x - 1) % self.WIDTH
                right_coord = (x + 1) % self.WIDTH
                top_coord = (y - 1) % self.HEIGHT
                bottom_coord = (y + 1) % self.HEIGHT

                # Count the number of living neighbors:
                num_neighbors = 0
                if self.next_cells[left_coord][top_coord] == '#':
                    num_neighbors += 1 # Top-left neighbor is alive.
                if self.next_cells[x][top_coord] == '#':
                    num_neighbors += 1 # Top neigbor is alive.
                if self.next_cells[right_coord][top_coord] == '#':
                    num_neighbors += 1 # Top-right neighbor is alive.
                if self.next_cells[left_coord][y] == '#':
                    num_neighbors += 1 # Left neighbor is alive.
                if self.next_cells[right_coord][y] == '#':
                    num_neighbors += 1 # Right neighbor is alive.
                if self.next_cells[left_coord][bottom_coord] == '#':
                    num_neighbors += 1 # Bottom-left coord is alive.
                if self.next_cells[x][bottom_coord] == '#':
                    num_neighbors += 1 # Bottom coord is alive.
                if self.next_cells[right_coord][bottom_coord] == '#':
                    num_neighbors += 1 # Bottom-right coord is alive.

                # Set cell based on Conway's Game of Life rules:
                if self.next_cells[x][y] == '#' and (num_neighbors == 2 or
                                             num_neighbors == 3):
                    # Living cells with 2 or 3 neighbors stay alive:
                    self.next_cells[x][y] = '#'
                elif self.next_cells[x][y] == ' ' and num_neighbors == 3:
                    # Dead cells with 3 neighbors become alive:
                    self.next_cells[x][y] = '#'
                else:
                    # Everything else dies or stays dead:
                    self.next_cells[x][y] = ' '
    
    def display(self):
        """Displays Conway's game."""
        print('\n\n\n\n\n') # Separate each step with newlines.
        current_cells = copy.deepcopy(self.next_cells)

        # Print current_cells on the screen:
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                print(current_cells[x][y], end='') # Print the '#' or a space.
            print() # Prints a new line at the end of the row.

