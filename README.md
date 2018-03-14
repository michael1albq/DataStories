
# Overview & Requirements

* What is the purpose of this repository? *
This repository is used to generate an image for each paragraph of a song. 

* How does it work? *
Given the lyrics as input, the algorithm first determines the keywords using RAKE (Rapid Automated Keyphrase Extraction) and then compares the chosen keywords with the list of image tags of these corresponding keywords using the Pixabay API (which allows for free image querying) and determines the best match using our algorithm (as described in the ppt attached).

* How do I test this out? *
All the code is in the notebook `Song_Visualizer.ipynb`. Examples are included in this repository. To be able to test out this algorithm, you will need to (1) install dependencies on Python (primarily RAKE), (2) download the pre-trained Google News Word2Vec model(~1.5 GB) and (3) lookup the song number of the chosen song in songdata.csv. 

# Usage

1. `$ git clone https://github.com/michael1albq/DataStories.git`
2. Download `GoogleNews-vectors-negative300.bin` (put it in the project root directory or edit the ipynb to update location).
3. Open `songdata.csv` (sourced from [Kaggle](https://www.kaggle.com/mousehead/songlyrics) and search for the song). Search for a song and use (rownumber - 2) as the index in the next step.
4.  Open `Song_Visualizer.ipynb` with jupyter notebook.
5.  Run to explore

# Additional Information with Links 

* [User Survey](https://docs.google.com/forms/d/e/1FAIpQLSckLEtQPsgyT_NrF5IOTU3BKEm7FV5h9BZmHeeoVMfPNmxWhg/viewform)

Our User Survey indicated that our algorithm performed within ~90% of a human picking with similar restrictions with an average of ~3.0 (algorithm) vs. ~3.3 (human). 

* [Lyrics Video - Country Roads (John Denver)](https://youtu.be/WKFEdOjgZUM)

The Lyrics Video shows the algorithm in action for the song 'Country Roads' including the keywords/image tag matrix and corresponding scores of candidate images.

* [Algorithm](https://github.com/michael1albq/DataStories/blob/master/Song_Visualizer.ipynb)
The algorithm used to generate the code.

# Project Team
This project was carried out for a class on Data Stories at Rutgers U. by:

* Michael Albuquerque (ma1333@rutgers.edu)
* Enkai Ji 
* SP Kumar (sp1381@scarletmail.rutgers.edu)


# References

* [Song Dataset](https://www.kaggle.com/mousehead/songlyrics)
* [Key-Word Extraction Algorithm](https://github.com/csurfer/rake-nltk)
