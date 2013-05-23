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
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(order_id, list_of_values):
    # list_of_records
    orders = []
    line_items = []
    for v in list_of_values:
      if v[0] == 'order':
        orders.append(v)
      else:
        line_items.append(v)

    for v in orders:
      for w in line_items:
        mr.emit(v + w)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
