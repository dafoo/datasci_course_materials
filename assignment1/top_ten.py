import sys
import json
import re

def hw(tweet_file):
  scores = {} # initialize an empty dictionary
  r = re.compile('#')
  for line in tweet_file:
   json_data = json.loads(line)
   if 'entities' in json_data.keys():
    # print json_data['entities']['hashtags']
    for hashtag in json_data['entities']['hashtags']:
       # print hashtag
       word = hashtag['text']
       # if word.find('#') == 0:
        # word = r.sub('', word)
       if word in scores:
         scores[word] += 1
       else:
         scores[word] = 1
  print_count = 0
  for key,value in sorted(scores.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    if print_count < 10:
      print (key.encode('ascii', 'replace') + " " + str(float(value)))
      print_count += 1

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
