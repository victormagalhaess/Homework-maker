import Algorithmia
import json
import os

def search(theme, lang):
    print("Input " + theme + " received with success! Searching on Wikipedia...")
    wikipediaDirtyData = dowloadWikipediaData(theme, lang)
    return wikipediaDirtyData
    wikipediaCleanData = cleanWikipediaData(wikipediaDirtyData)
    searchData = breakDataInSentences(wikipediaCleanData)
    return searchData


def dowloadWikipediaData(theme, lang):
    input = {
    "articleName": theme,
    "lang": lang
    }

    with open('credentials/algorithmia.json') as json_file:
        credentials = json.load(json_file)
    apiKey = credentials['apiKey']
    
    client = Algorithmia.client(apiKey)
    algo = client.algo('web/WikipediaParser/0.1.2')
    algo.set_options(timeout=300)
    wikiResult = algo.pipe(input).result
    return wikiResult


def cleanWikipediaData(dirtyData):
    pass


def breakDataInSentences(cleanData):
    pass
