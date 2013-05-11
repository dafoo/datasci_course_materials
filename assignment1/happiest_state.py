import sys
import json

def hw(sent_file, tweet_file):
  scores = {} # initialize an empty dictionary
  state_scores = {}
  for line in sent_file:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.
  for line in tweet_file:
    json_data = json.loads(line)
    if "place" in json_data.keys() and json_data["place"] and "country_code" in json_data["place"].keys() and json_data["place"]["country_code"] == "US" and "full_name" in json_data["place"]:
      full_name = json_data["place"]["full_name"]
      location = full_name.split()
      cur_state = location[-1]
      # print location[-1]
      if "text" in json_data:
        words = json_data["text"].split()
        sentiment = 0
        # print words
        for word in words:
          if word in scores:
            sentiment = sentiment + scores[word]
        # print sentiment
        if cur_state in state_scores.keys():
          state_scores[cur_state] += sentiment
        else:
          state_scores[cur_state] = sentiment
  # print state_scores
  for key,value in sorted(state_scores.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print key
    break

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
