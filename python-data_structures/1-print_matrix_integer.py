#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
  for row in matrix:
    for mat_num in row:
      print("{}".format(mat_num),end=" ")
    print()
    