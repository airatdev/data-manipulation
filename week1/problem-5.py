import sys
import json

state_codes = {
  'AK': 'Alaska',
  'AL': 'Alabama',
  'AR': 'Arkansas',
  'AS': 'American Samoa',
  'AZ': 'Arizona',
  'CA': 'California',
  'CO': 'Colorado',
  'CT': 'Connecticut',
  'DC': 'District of Columbia',
  'DE': 'Delaware',
  'FL': 'Florida',
  'GA': 'Georgia',
  'GU': 'Guam',
  'HI': 'Hawaii',
  'IA': 'Iowa',
  'ID': 'Idaho',
  'IL': 'Illinois',
  'IN': 'Indiana',
  'KS': 'Kansas',
  'KY': 'Kentucky',
  'LA': 'Louisiana',
  'MA': 'Massachusetts',
  'MD': 'Maryland',
  'ME': 'Maine',
  'MI': 'Michigan',
  'MN': 'Minnesota',
  'MO': 'Missouri',
  'MP': 'Northern Mariana Islands',
  'MS': 'Mississippi',
  'MT': 'Montana',
  'NA': 'National',
  'NC': 'North Carolina',
  'ND': 'North Dakota',
  'NE': 'Nebraska',
  'NH': 'New Hampshire',
  'NJ': 'New Jersey',
  'NM': 'New Mexico',
  'NV': 'Nevada',
  'NY': 'New York',
  'OH': 'Ohio',
  'OK': 'Oklahoma',
  'OR': 'Oregon',
  'PA': 'Pennsylvania',
  'PR': 'Puerto Rico',
  'RI': 'Rhode Island',
  'SC': 'South Carolina',
  'SD': 'South Dakota',
  'TN': 'Tennessee',
  'TX': 'Texas',
  'UT': 'Utah',
  'VA': 'Virginia',
  'VI': 'Virgin Islands',
  'VT': 'Vermont',
  'WA': 'Washington',
  'WI': 'Wisconsin',
  'WV': 'West Virginia',
  'WY': 'Wyoming'
}

def main():
  afinn_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])

  sentiment_scores = {}
  states = {}

  for line in afinn_file:
    term, term_score  = line.split('\t')
    sentiment_scores[term] = int(term_score)

  for line in tweet_file:
    tweet_score = 0
    parsed = json.loads(line)

    if parsed.has_key('text'):
      if parsed['place'] != None and parsed['place']['country_code'] == 'US':
        state_name = parsed['place']['full_name'].split()[1]

        if state_codes.has_key(state_name):
          words = parsed['text'].split(' ')

          for word in words:
            word = word.lower()

            if sentiment_scores.has_key(word):
              tweet_score += sentiment_scores[word]

          states[state_name] = tweet_score

  print sorted(states.items(), key=lambda x:x[1])[-1][0]

if __name__ == '__main__':
  main()
