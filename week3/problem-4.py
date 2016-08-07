import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
  mr.emit_intermediate(''.join(sorted([record[0], record[1]])), [record[0], record[1], 1])

def reducer(key, list_of_values):
  if len(list_of_values) == 1:
    mr.emit((list_of_values[0][1], list_of_values[0][0]))
    mr.emit((list_of_values[0][0], list_of_values[0][1]))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
