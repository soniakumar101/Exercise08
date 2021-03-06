#!/usr/bin/env python

import sys
import random
# from key.txt import ConsumerKeyAPIKey, ConsumerSecretAPISecret, AccessToken, AccessTokenSecret
import twitter

ConsumerKeyAPIKey = '27UK15mUaqcXUjPwwOFxWaI8n'
ConsumerSecretAPISecret = 'c2hW1dvNsJz9BQHG1Vkfb9Xz3it0xgknMQxsuVHMB7RY4e2AeU'
AccessToken = '2851249448-J0oLZwf8tsMZBuiuksYeUg5gTxj1iO3RpmuF0xl'
AccessTokenSecret = 'Plbm2k4jji2PrWCuhjNiaCCNkFk3LxJePoQIElituaoB5'

api = twitter.Api(consumer_key=ConsumerKeyAPIKey,
                  consumer_secret=ConsumerSecretAPISecret,
                  access_token_key=AccessToken,
                  access_token_secret=AccessTokenSecret)



def make_chains(words,x):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    words_list = []
    words_list = words.strip().split()
    chains = {}
    #print "Choose a number between one and ten."
    #x = int(raw_input())
    # list[x] = [:x + 1]
    for i in range(len(words_list)-x):
        # word_one = words_list[i]
        # word_two = words_list[i+1]
        # word_three = words_list[i+2]
        # d = {key: [word_one, word_two]}
        key = tuple(words_list[i:(i+x)])
        # print "Key: ", key
        word_next = words_list[i+x]
        # print "Word next: ", word_next
        # d[key].append(word_two)
        #value = [word_three]
        if key not in chains:
            chains[key]=[word_next]
        else:
            chains[key].append(word_next)
    return chains

def make_text(chains,x):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    keys = chains.keys()  # [("word_one", "word_two")]
    k = random.choice(keys) # ("word_one", "word_two")
    output = list(k)
    while k in chains and len(" ".join(output)) < 135:
        p_values = chains[k]
        value = random.choice(p_values) # "word_three"
        output.append(value)
        #output = [k[0],  k[1],  value] # "word_oneword_twoword_three"
        # printout = (" ".join(k) + " " + value)
        # print printout
        k = tuple(output[-x:])
    return output
 
# def make_tweet(random_text):
#     while len(random_text) > 1005:
#         random_text.pop()

#     shorter_text = random_text
#     # print type(shorter_text)

#     # for words in random_text:
#     #     if not "." in words: 
#     #         continue

#     return shorter_text

def main(filename):
    args = sys.argv
    script, filename = args

    # Change this to read input_text from a file
    f = open(filename)
    words = f.read()
    # print "Choose a number between one and ten."
    # x = int(raw_input())
    x = 2

    chain_dict = make_chains(words,x)
    # print chain_dict
    random_text = make_text(chain_dict, x)
    # tweet_text = make_tweet(random_text)
    # print type(random_text)
    print " ".join(random_text)
    api.PostUpdate(" ".join(random_text))

if __name__ == "__main__":
    main("pythonmashup.txt")