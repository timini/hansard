# hansard project

I'm just starting out with an analysis of the [UK Parlimentary Archive](http://www.hansard-archive.parliament.uk/). The broad goals at the minute are to create language models from the speaches given by UK officials in the House of Commons and the House of Lords. I have many interestng questions to answer about this dataset, please take a look at the issues here to see some that are being investigated.

#### Getting the data

There are 2 ways to get the data

 - Download the digitised archives as XML files from the [hansard archive](http://www.hansard-archive.parliament.uk/).
 - Access the data using the rails and solr based API build by [millbank systems](http://hansard.millbanksystems.com/).

This project contains scripts to access both: A small bash file in the `data` folder can be used to automate downloading of XML files, and a scrapy project for scraping data from the API. use the command `scrapy crawl comments -o comments.json` to extract data from the API.

#### Analysis

Data analysis is prototyped using ipython notebooks. You can view them using the notebook viewer:

1. [Data Wrangling](http://nbviewer.ipython.org/github/timini/hansard/blob/master/01%20API%20Wrangling.ipynb) Obtaining data from the API, cleaning it and converting it to a useful datastructure.
2. [Generating model representations of the data](http://nbviewer.ipython.org/github/timini/hansard/blob/master/02%20Data%20cleaning%2C%20vector%20representations.ipynb) The raw text is cleaned of punctuation and tokenised. Bag of Words and IF/IDF models are created.
3. [PCA and clustering of Speakers](http://nbviewer.ipython.org/github/timini/hansard/blob/master/03%20PCA%20.ipynb) - do labeled groups cluster using PCA? i.e do speakers from the house of commons / lords cluster together? Do speakers from the different poitical parties cluster together?

#### Related Projects

 - Jun Hao has a [notebook covering topic modelling](http://hojunhao.github.io/sgparliament/LDA.html) of the Singapore Parliamentary Debate Records.
 - http://www.theyworkforyou.com/
 - https://www.writetothem.com/
 - https://www.mysociety.org/

#### development

this project is using python virtual environments to manage the dependancies locally instead of installing packages globaly on your system. to setup a new virtual environmant use

```
# initialise your virtual environment
$ pyvenv venv 
# activate the virtual environment
source ./venv/bin/activate
# install the project dependancies
pip install -r requirements.txt
```

#### Contributers

 - (Jun hao)[https://github.com/hojunhao]
