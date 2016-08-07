import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
  mr.emit_intermediate(record[1], record)

def reducer(key, list_of_values):
  for value in list_of_values:
    if value[0] == 'line_item':
      mr.emit(list_of_values[0] + value)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
