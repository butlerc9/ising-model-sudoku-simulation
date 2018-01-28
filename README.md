# Sudoku Simulated Annealing: Duality of Non-Symmetric 9-State Potts Model

In this experiment the metropolis algorithm combined with simulated annealing was used to investigate the change in energy of a 2D ising model. This code was then adapted and was directly applied to the solution of Sudoku puzzles of various difficulties. Comparisons between the 9-State Potts model are also evident from the second order phase change which occurs at a temperature of 0.75

Sudoku has proved to be an insightful tool to help us explore more unique aspects of magnetic behaviour. Second order phase transitions were observed in both the Ising model and Sudoku puzzles. However the critical temperature for Sudoku was only calculated to be 0.75 whereas the Ising model had a temperature of ($2.5\pm 0.3$) with a theoretical critical temperature of 2.27.
## Getting Started

To use this code you must run the code in `randommatrixgeneratr.py` and import isingfunctions and `randommatrixgenerator.py`. These will import the code nessesscary to make the code. Once imported then you can run the `IsingModelTest.py`. This code is ready to run at this point and you will be faced with a live plot. Simply comment out 2 of the 3 options to view either; a live ising model plot, a live magnetiztion plot or a live energy plot.

### Prerequisites

A fresh installation of python etc. On top of this youll need the default packages numpy,scipy,matplotlib etc.


### Switching to Sudoku

In the sudoku branch there is `sudoku.py` which is ready to run. All of the puzzles havent been included as extras so as to not add the effort of importing code. In some earlier version Isingfunctions was importable and the cooling function based on another of my projects (a coffee cooling ODE solver) was used to anneal the puzzle but that cooled too quickly and so was discarded.



## Authors

* **Cormac Butler** - *Initial work* - [Cormac Butler](https://github.com/Butlerc9)

## Acknowledgments

* Idea for the simulated annealing of Sudoku from https://github.com/grubino/sudoku_anneal
* Template for readme: https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
