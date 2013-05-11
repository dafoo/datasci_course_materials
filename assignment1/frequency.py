import sys
import json

def hw(tweet_file):
  scores = {} # initialize an empty dictionary
  total_count = 0
  for line in tweet_file:
    json_data = json.loads(line)
    if "text" in json_data:
      words = json_data["text"].split()
      # print words
      for word in words:
        total_count += 1;
        if word in scores:
          scores[word] += 1
        else:
          scores[word] = 1
  for word in scores.keys():
    print (word.encode('ascii', 'replace') + " " + str(scores[word]/float(total_count)))

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
