# -*- coding: utf-8 -*-
import scrapy
import json
from BeautifulSoup import BeautifulSoup
from hansard.items import HansardComment

START_URLS = []
for year in range(1800, 2014):
    for month in ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']:
        for day in range(1, 32):
            START_URLS.append('http://hansard.millbanksystems.com/sittings/%s/%s/%s.js' % (year, month, day))

sitting_kind_url_fragments = {
    "house_of_commons_sitting":"/commons/",
    "westminster_hall_sitting":"/westminster_hall/",
    "commons_written_answers_sitting":"/written_answers/",
    "house_of_lords_sitting":"/lords/",
    "lords_written_answers_sitting":"/written_answers/",
    "grand_committee_report_sitting":"/grand_committee_report/",
    "commons_written_statements_sitting":"/written_answers/",
    "lords_written_statements_sitting":"/written_answers/",
    # TODO: there is some stuff missing here
    # ???? : "/lords_reports/"
}

class CommentsSpider(scrapy.Spider):
    start_urls = START_URLS
    name = "comments"
    allowed_domains = ["hansard.millbanksystems.com"]

    def parse(self, response):
        sittings = json.loads(response.body)
        date = '/'.join(response.url[:-3].split('/')[-3:])
        for url in ["http://hansard.millbanksystems.com" +
                    sitting_kind_url_fragments[sit.keys()[0]] +
                    date +
                    '.js'
                    for sit in sittings]:
            yield scrapy.Request(url, callback=self.parse_sittings)

    def parse_sittings(self, response):
        for sitting in json.loads(response.body):
            sitting = sitting[sitting.keys()[0]]
            for section in sitting['top_level_sections']:
                section = section[section.keys()[0]]
                url = response.url[:-3] + '/' + section['slug']
                yield scrapy.Request(url, callback=self.parse_sections)

    def parse_sections(self, response):
        html = BeautifulSoup(response.body)
        contributions = html.findAll("div",
                        {"class":lambda x: x and 'member_contribution' in x.split()})
        for contrib in contributions:
            try:
                author_id = dict(contrib.findAll("cite", {"class":lambda x: x and 'author' in x.split()})[0].find("a").attrs)["href"]
                author_name = ""
                house = response.url.split('/')[3]
                content = ' '.join([para.text for para in contrib.findAll("p")])
                date = response.url.split('/')[-4:-1]
                comment = HansardComment(
                    author_id=author_id,
                    author_name=author_name,
                    house=house,
                    content=content,
                    date=date,
                )
                yield comment
            except Exception as e:
                pass
