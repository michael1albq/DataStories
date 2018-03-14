# Project: DataStories
# Author: Michael Albuquerque
# Date Created: 10/31/17
# Python Version: 3.6.2

# Description: 

from pycorenlp import StanfordCoreNLP

if __name__ == '__main__':
    nlp = StanfordCoreNLP('http://localhost:9000')
    text = ("Almost heaven, West Virginia,\
Blue ridge mountain, Shenandoah river,\
Life is old there, older than the trees,\
Younger than the mountains, blowing like a breeze")

    output = nlp.annotate(text, properties={
        'annotators': 'tokenize,ssplit,pos,depparse,parse',
        'outputFormat': 'json'
    })
    print(output['sentences'][0]['parse'])
    output = nlp.tokensregex(text, pattern='/West|Virginia/', filter=False)
    print(output)
    output = nlp.semgrex(text, pattern='{tag: NN}', filter=False)
    print(output)
