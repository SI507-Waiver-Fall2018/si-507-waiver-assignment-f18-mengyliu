# these should be the only imports you need
import tweepy
import nltk
import json
import sys

# write your code here
# usage should be python3 part1.py <username> <num_tweets>

stopwords=['http', 'https', 'RT']


def main():
	if len(sys.argv) != 3:
		print('usage should be python3 part1.py <username> <num_tweets>')
		sys.exit(1)

	username = sys.argv[1]
	num_tweets = int(sys.argv[2])

	#consumer key, consumer secret, access token, access secret, used for OAuth
	consumer_key = "nhGKB80ht4DUjJpP4ACfZiZrb"
	consumer_secret = "dCsXEeohbB7WSojq58C3P4VQaiVL9ZIhnSCWxp3CFRUdvaPKXQ"
	access_token = "821332816071950336-ZwYe8YRIpDFSvCErIaSIYjO5BCC2pGj"
	access_token_secret = "Qui1mroctHMdnS5G6xVa6hcWh4MXo8EGeIgpuJPqTjhV9"

	#OAuth
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	#find the user's all tweets
	original_count = 0
	favorite = 0
	retweet = 0
	word_list = []
	tweets = api.user_timeline(screen_name=username, count=num_tweets, tweet_mode="extended")
	for tweet in tweets:
		tweet_json = json.dumps(tweet.full_text)
		tweet_token = [word for word in nltk.word_tokenize(tweet_json) if word.isalpha() and word not in stopwords]
		tweet_tagged = nltk.pos_tag(tweet_token)
		for tt in tweet_tagged:
			word_list.append(tt)
		if 'RT @' not in tweet.full_text:
			original_count += 1
			favorite += tweet.favorite_count
			retweet += tweet.retweet_count

	freDist = nltk.FreqDist(word_list).most_common()
	nouns = sorted([(tt[0][0], tt[1]) for tt in freDist if tt[0][1] == 'NN'], key= lambda x: x[1], reverse=True)[:5]
	verbs = sorted([(tt[0][0], tt[1]) for tt in freDist if tt[0][1] == 'VB'], key= lambda x: x[1], reverse=True)[:5]
	adjs = sorted([(tt[0][0], tt[1]) for tt in freDist if tt[0][1] == 'JJ'], key= lambda x: x[1], reverse=True)[:5]
	# except Exception as error:
	# 	print('cannot found this user')
	# 	sys.exit(1)	
	print('USER: {}'.format(username))
	print('TWEETS ANALYZED: {}'.format(num_tweets))	


	print('VERBS:',end=' ')
	for v in verbs:
		print ('{}({})'.format(*v),end=' ')
	print('')
	print('NOUNS:',end=' ')
	for n in nouns:
		print ('{}({})'.format(*n),end=' ')
	print('')
	print('ADJECTIVES:',end=' ')
	for a in adjs:
		print ('{}({})'.format(*a),end=' ')
	print('')
	print('ORIGINAL TWEETS: {}'.format(original_count))
	print('TIMES FAVORITED (ORIGINAL TWEETS ONLY): {}'.format(favorite))
	print('TIMES RETWEETED (ORIGINAL TWEETS ONLY): {}'.format(retweet))

	f = open("noun_data.csv","w+")
	f.write("Noun,Number\n")
	for n in nouns:
		f.write("{},{}\n".format(*n))
	f.close()




if __name__ == "__main__":
    main()
