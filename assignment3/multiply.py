import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    matrix_dimension = 5

    matrix_name = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    if matrix_name == 'a':
      for ii in range(0, matrix_dimension):
        mr.emit_intermediate(str(i)+str(ii), record)
    else: # b matrix
      for ii in range(0, matrix_dimension):
        mr.emit_intermediate(str(ii)+str(j), record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    # total = 0
    new_val = 0
    row = 0
    col = 0
    for v in list_of_values:
      if v[0] == 'a':
        a_col = v[2]
        row = v[1]
        for w in list_of_values:
          if w[0] == 'b' and w[1] == a_col:
            new_val += v[3] * w[3]
            col = w[2]
    mr.emit((row, col, new_val))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
