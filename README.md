# hansard project

I'm just starting out with an analysis of the [UK Parlimentary Archive](http://www.hansard-archive.parliament.uk/). The broad goals at the minute are to create language models from the speaches give by UK officials in the House of Commons and the House of Lords. I have many interestng questions to answer about this dataset, please take a look at the issues here to see some that are being investigated.

#### Getting the data

There are 2 ways to get the data

 - Download the digitised archives as XML files from the [hansard archive](http://www.hansard-archive.parliament.uk/).
 - Access the data using the rails and solr based API build by [millbank systems](http://hansard.millbanksystems.com/).

This project contains scripts to access both: A small bash file in the `data` folder can be used to automate downloading of XML files, and a scrapy project for scraping data from the API. use the command `scrapy crawl comments -o comments.json` to extract data from the API.

#### Viewing the notebooks

- http://nbviewer.ipython.org/github/timini/hansard/tree/master/
