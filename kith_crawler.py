import scrapy


class KithSpider(scrapy.Spider):
    name = "kith"

    def start_requests(self):
        start_url = [
            'https://kith.com/',
        ]
        for url in start_url:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)