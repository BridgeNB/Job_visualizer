# This is a crawler for clawing job information
# from monster.com

# packages
import urllib2
import re

class monsterCrawler:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  # what is this
        # Initiate the header
        self.headers = {'User-Agent': self.user_agent}
        # An array to element
        self.jobs = []
        # Crawler status
        self.enable = False

    # Obtain HTML
    def getPage(self, pageIndex):
        try:
            url = 'http://www.monster.com/jobs/search/?q=software&page=' + str(pageIndex)
            # Obtain request object
            req = urllib2.Request(url)
            # Obtain response object
            res = urllib2.urlopen(req)
            # decode the page
            pageCode = res.read().decode('utf-8')
            return pageCode
        except urllib2.HTTPError, e:
            if hasattr(e, 'reason'):
                print u'Connection error, reason: ', e.reason
                return None

    # Obtain page items
    def getPageJobs(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        pageInfo = []
        # check if page successfully loaded
        if not pageCode:
            print u'Page load error!'
            return None

        # ### Match job ID and job title
        pattern = re.compile(ur'"url" : "http://jobview.monster.com/(.*).aspx"')
        items = pattern.findall(pageCode)

        for item in items:
            pageInfo.append(item)

        return pageInfo

    # Load page and add jobs to global list
    def loadPage(self):
        if self.enable == True:
            pageInfo = self.getPageJobs(self.pageIndex)
            if pageInfo:
                self.jobs.append(pageInfo) # add job to global list
                self.pageIndex += 1        # load next page

    # Print all jobs in one page
    def getJobs(self, jobs, page):
        for job in jobs:
            print "Page No. %s, job info is: %s " %(page, job)

    # Start the crawler
    def start(self):
        print u'Job crawler started, press enter to view result, press q to quit'

        self.enable = True
        curPage = 0

        while self.enable:
            # Command
            input = raw_input()
            self.loadPage()
            # Quit if command is q
            if input == 'q':
                self.enable = False
                break
            elif len(self.jobs) > 0:
                jobs = self.jobs[0]
                curPage += 1
                del self.jobs[0]
                self.getJobs(jobs, curPage)

            print input

crawler = monsterCrawler()

crawler.start()
