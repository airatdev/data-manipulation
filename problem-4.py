import sys
import json

def main():
  tweet_file = open(sys.argv[1])

  occurences = {}
  total_words = 0

  for line in tweet_file:
    parsed = json.loads(line)

    if parsed.has_key('text'):
      words = parsed['text'].encode('utf-8').split()

      for word in words:
        word = word.lower()
        total_words += 1

        if not occurences.has_key(word):
          occurences[word] = 1

        occurences[word] += 1

  for word, count in occurences.items():
    print word + " " + float(count) / total_words

if __name__ == '__main__':
  main()
