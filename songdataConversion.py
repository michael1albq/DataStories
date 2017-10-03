# Project: DataStories
# Author: Michael Albuquerque
# Date Created: 10/3/17
# Python Version: 3.6.2

# Description:

import pandas as pd

songDF = pd.read_csv("songdata.csv", usecols=["artist", "song", "text"], nrows=10)
songDF.to_csv("testSongDF.", index = False)