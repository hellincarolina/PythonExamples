# About
This repository contains python libraries with functions to provide the following features:
1. Get the first repeated value between two list of integers
2. Given a directory, get the first file that meets the following conditions:
  a. The owner is an administrator
  b. It's an executable file
  c. The file has a size lower than 14*2^20
3. Given a list of 0's and 1's, get the minimum permutations to be done so that the list ends fully interspersed

Unit tests are provided as well using Pytest. 

# How to setup
No additional work is needed to use the functions. 

## Unit tests
To run the test cases it's required to install Pytest. 

Pytest downloading and documentation available in: https://pypi.org/project/pytest/

It's required to create an empty directory name "emptydirectory" inside test_data directory in order to successfully run the unit tests on test_find_file.py. However, you can change the data to run the tests by replacing the directories/files with existing ones on your local machine.

Run the unit test by executing the command "pytest" on a command line console, inside the test directory.

`../test >> pytest`





