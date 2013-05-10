import sys
import json

def hw(sent_file, tweet_file):
  scores = {} # initialize an empty dictionary
  new_words = {}
  for line in sent_file:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.
  for line in tweet_file:
    json_data = json.loads(line)
    if "text" in json_data:
      words = json_data["text"].split()
      sentiment = 0
      # print words
      for word in words:
        if word in scores:
          sentiment = sentiment + scores[word]
      for word in words:
        if word not in scores:
          if word in new_words:
            new_words[word] += sentiment
          else:
            new_words[word] = sentiment
  for word in new_words.keys():
    print (word.encode('ascii', 'replace') + " " + str(new_words[word]))

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
