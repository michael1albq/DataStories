# Project: DataStories
# Author: Michael Albuquerque
# Date Created: 10/3/17
# Python Version: 3.6.2

# Description: Uses Rake Algorithm to automatically extract keywords from a song lyrics file

from rake_nltk import Rake
import pandas as pd

df = pd.read_csv("testSongDF.csv")

test1 = df['text'][0]
print(test1)

r = Rake()
r.extract_keywords_from_text(test1)
print(r.get_ranked_phrases())
