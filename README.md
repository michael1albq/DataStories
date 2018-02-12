
# Overview & Requirements

`Song_Visualizer.ipynb` is used to generate an image for each paragraph of a song. Examples are included in this repository.

To run this, you will need to install dependencies, primarily RAKE, download the pre-trained Google News Word2Vec model(~1.5 GB) and lookup the song number in songdata.csv. 

# Usage
1. `$ git clone https://github.com/michael1albq/DataStories.git`
2. Download `GoogleNews-vectors-negative300.bin` and put it in the project root directory.
3. Open `songdata.csv` (sourced from [Kaggle](https://www.kaggle.com/mousehead/songlyrics) and search for the song). Search for a song and use (rownumber - 2) as the index in the next step.
4.  Open `Song_Visualizer.ipynb` with jupyter notebook.
5.  Run each cell from the top and explore the results

# Links 

* [User Survey](https://docs.google.com/forms/d/e/1FAIpQLSckLEtQPsgyT_NrF5IOTU3BKEm7FV5h9BZmHeeoVMfPNmxWhg/viewform)
* [Lyrics Video - Country Roads (John Denver)](https://youtu.be/WKFEdOjgZUM)

* [Manual](https://docs.google.com/document/d/10HvHlIFRJy6NmU9uxNbhjY92KNjwS3qWGhpdtbY_GE4/edit?pli=1)
* [Algorithmic](https://github.com/michael1albq/DataStories/blob/master/Song_Visualizer.ipynb)

# Project Team
* Michael Albuquerque (ma1333@rutgers.edu)
* Enkai Ji 
* SP Kumar (sp1381@scarletmail.rutgers.edu)


# References
* [Song Dataset](https://www.kaggle.com/mousehead/songlyrics)
* [Key-Word Extraction Algorithm](https://github.com/csurfer/rake-nltk)
