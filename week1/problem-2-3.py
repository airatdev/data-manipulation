import sys
import json

def main():
  afinn_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])

  sentiment_scores = {}
  unknown_words_scores = {}

  for line in afinn_file:
    term, term_score  = line.split('\t')
    sentiment_scores[term] = int(term_score)

  for line in tweet_file:
    tweet_score = 0
    parsed = json.loads(line)

    if parsed.has_key('text'):
      words = parsed['text'].split(' ')

      for word in words:
        word = word.lower()

        if sentiment_scores.has_key(word):
          tweet_score += int(sentiment_scores[word])

      if tweet_score != 0:
        for word in words:
          if not sentiment_scores.has_key(word):
            unknown_words_scores[word] = 1 if tweet_score > 0 else -1

    for key in unknown_words_scores:
      print key, unknown_words_scores[key]

if __name__ == '__main__':
  main()
