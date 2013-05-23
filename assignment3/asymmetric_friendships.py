import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # person = record[0]
    # friend = record[1]
    li = [record[0], record[1]]
    li.sort()
    key = '/'.join(li)
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    if len(list_of_values) < 2:
      mr.emit((list_of_values[0][0], list_of_values[0][1]))
      mr.emit((list_of_values[0][1], list_of_values[0][0]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
