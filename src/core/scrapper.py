from collections import Counter

import nltk
import requests
from textblob import TextBlob

import settings

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

res = requests.get(settings.URL)
text = res.text
blob_object = TextBlob(text)
tags = blob_object.tags
tag_list = []
for tag in tags:
    tag_list.append(tag[1])

counted_tags = Counter(tag_list)
print(counted_tags)
