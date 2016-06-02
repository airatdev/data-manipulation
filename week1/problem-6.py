import sys
import json

def main():
  tweet_file = open(sys.argv[1])

  occurences = {}

  for line in tweet_file:
    parsed = json.loads(line)

    if parsed.has_key('entities') and parsed['entities']['hashtags']:
      for hashtag in parsed['entities']['hashtags']:
        if not occurences.has_key(hashtag['text']):
          occurences[hashtag['text']] = 1
        else:
          occurences[hashtag['text']] += 1

  sorted_occurences = sorted(occurences.items(), key=lambda x:x[1])
  sorted_occurences.reverse()

  for hashtag, count in sorted_occurences[0:10]:
    print hashtag, count

if __name__ == '__main__':
  main()
