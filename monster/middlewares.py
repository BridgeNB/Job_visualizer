__author__ = 'zhengyangqiao'

import random
import base64
import os
from scrapy.conf import settings

class RandomUserAgent(object):
    """ Randomly use a list of IPs to prevent spider from banned
    """
    def process_request(self, request, spider):
        ua = random.choice(settings.get('USER_AGENT_LIST'))
        if ua:
            request.headers.setdefault('User-Agent', ua)

class RandomProxy(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = settings.get('HTTP_PROXY')

