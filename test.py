import re

# To Read Tweets directly from Program:
tweet = """Most employees fulfilled with used hardware based on device turns four years old.
Some job categories (hardware or software developer, technical sales, etc.) are eligible at three years.
Recognizing that employee job roles or device request qualities and inventory allows , the CIO considers requests for early refresh.
When submitting, provide a detailed justification as to requirements can change at any time why a new device is needed.
Devices reviews  an early refresh request the request if the, Devices honors the request.
Early refresh requests  are eligible for refresh when their primary computing may be funding levels and available"""

# To Read Tweets from File:
# with open("tweets.txt", "r") as f:
#     tweet = f.read()


tot_no_of_words = len(tweet.split())
half_of_words = tot_no_of_words // 2
list_of_abusive_words = ["device", "refresh"]


abusive_words = 0

for abusive_word in list_of_abusive_words:
    abusive_words += len(re.findall(abusive_word, tweet))*2

if abusive_words == 0:
    print("Pure Content.")
elif tot_no_of_words > abusive_words:
    print("Less Abusive.")
else:
    print("More Abusive.")





