import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
  if record[0] == 'a':
    for k in range(5):
      mr.emit_intermediate(str(record[1]) + str(k), record)
  else:
    for k in range(5):
      mr.emit_intermediate(str(k) + str(record[2]), record)

def reducer(key, list_of_values):
  result = 0

  for a in list_of_values:
    for b in list_of_values:
      if a[0] == 'a':
        if a[2] == b[1] and b[0] == 'b':
          product = a[3] * b[3]
          result += product

  mr.emit((int(key[0]), int(key[1]), result))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
