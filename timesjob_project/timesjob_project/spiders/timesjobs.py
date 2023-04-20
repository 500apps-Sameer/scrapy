
import scrapy


class TimesjobsSpider(scrapy.Spider):
    name = 'timesjobs'
    # allowed_domains = ['https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35']
    start_urls = ['https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35']

    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'myoutput1.json'
    }

    def parse(self, response):
        title = response.xpath("//ul[@class='new-joblist']/li/header/h2/a/text()").getall()      
        job_d = response.xpath("//ul[@class='list-job-dtl clearfix']/li/text()").getall()
        company_name = response.xpath("//ul[@class='new-joblist']/li/header/h3/text()").getall()
        experience = response.xpath("//ul[@class='top-jd-dtl clearfix']/li//text()").getall()
        skills = response.xpath("//ul[@class='list-job-dtl clearfix']/li/span/text()").getall()

        for i in range(len(title)):
            yield {
                'title': title[i].strip(),
                'job_d': job_d[i].strip(),
                'company_name': company_name[i].strip(),
                'experience': experience[i].strip(),
                'skills': skills[i].strip(),
                
                }