#-*- coding: UTF-8 -*-

__author__ = 'zhengyangqiao'

import time
import scrapy
import json
import yaml
from scrapy.contrib.spiders import CrawlSpider
from monster.items import MonsterItem

class Monster_spider(CrawlSpider):
    # Name of the spider
    name = "monster_software"
    allowed_domains = ["monster.com"]
    # Temporally for software job
    start_urls = ["http://www.monster.com/jobs/search/?q=software"]

    def parse(self, response):
        # temp json response
        selectors = response.xpath('//script[@type="application/ld+json"]/text()').extract()
        # json_response = json.loads(response.body_as_unicode())
        # # loading time interval
        # time.sleep(5)


        items = []
        for sel in selectors:
            item = MonsterItem()
            # convert unicode to json
            json_sel2 = yaml.safe_load(sel)
            try:
                item['title']          = json_sel2['title']
                item['company']        = json_sel2['hiringOrganization']['name']
                item['job_state']      = json_sel2['jobLocation']['address']['addressRegion']
                item['job_city']       = json_sel2['jobLocation']['address']['addressLocality']
                item['des']            = json_sel2['description']
                item['date']           = json_sel2['datePosted']
            except Exception, e:
                print repr(e)
            # print(json_sel2['title'])
            items.append(item)
        return items
