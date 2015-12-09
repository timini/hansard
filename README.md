# hansard project

I'm just starting out with an analysis of the [UK Parlimentary Archive](http://www.hansard-archive.parliament.uk/). The broad goals at the minute are to create language models from the speaches give by UK officials in the House of Commons and the House of Lords. I have many interestng questions to answer about this dataset, please take a look at the issues here to see some that are being investigated.

#### Getting the data

There are 2 ways to get the data

 - Download the digitised archives as XML files from the [hansard archive](http://www.hansard-archive.parliament.uk/).
 - Access the data using the rails and solr based API build by [millbank systems](http://hansard.millbanksystems.com/).

This project contains scripts to access both: A small bash file in the `data` folder can be used to automate downloading of XML files, and a scrapy project for scraping data from the API. use the command `scrapy crawl comments -o comments.json` to extract data from the API.

#### Analysis

Data analysis is prototypes using ipython notebooks. You can view them using the notebook viewer:

1. [Data Wrangling](http://nbviewer.ipython.org/github/timini/hansard/blob/master/01%20API%20Wrangling.ipynb) Obtaining data from the API, cleaning it and converting it to a useful datastructure.
2. [Generating model representations of the data](http://nbviewer.ipython.org/github/timini/hansard/blob/master/02%20Data%20cleaning%2C%20vector%20representations.ipynb) The raw text is cleaned of punctuation and tokenised. Bag of Words and IF/IDF models are created.
3. [PCA and clustering of Speakers](http://nbviewer.ipython.org/github/timini/hansard/blob/master/03%20PCA%20.ipynb) - do labeled groups cluster using PCA? i.e do speakers from the house of commons / lords cluster together? Do speakers from the different poitical parties cluster together?
