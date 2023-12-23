# Naive BackTracking Sudoku Solver

The naive algorithm replaces the empty spaces with a digit which is not present in the given row or column or the 3x3 square it is in. It tries to place digits 1-9, if it fits, it moves to next cell and repeats, if the algorithm fails to fit a number, it backtracks to the previous cell and change its digit and tries again, this is the naive backtracting sudoku solver!!.

# Requirments:
- Python
  
## Usage
NOTE: there are two pre-defined sudokus namely, matrix and matrix2, change the argument passed in the function to get desired output of the sudoku

## Future updates
- add a GUI for better visuals

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## References

got the idea to do this from watching a video of ForrestKnight
