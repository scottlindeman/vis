import scrapy
from scrapy.contrib.loader import ItemLoader
from aviation.items import AviationItem

class AviationSpider(scrapy.Spider):
    name = "aviation"
    #allowed_domains = "http://aviation-safety.net"
    start_urls = ["http://aviation-safety.net/database/"]

    def parse(self, response):
        return self._database_parse(response)


    def _database_parse(self, response):
        for a in response.xpath('//div[@class="innertube"]//a[contains(@href, "dblist.php?Year=")]'):
            yield scrapy.Request(self.start_urls[0]+a.xpath('@href').extract()[0],
                                 callback=self._dblist_pagination_parse)

    def _dblist_pagination_parse(self, response):
        for a in response.xpath('//div[@class="pagenumbers"][1]/a'):
            yield scrapy.Request(self.start_urls[0]+'dblist.php'+a.xpath('@href').extract()[0],
                                 callback=self._dblist_parse)

        for r in self._dblist_parse(response):
            yield r

    def _dblist_parse(self, response):
        fs = None
        for tr in response.xpath('//div[@class="innertube"]//tr[position()>1]'):
            link = tr.xpath('td[1]//a/@href').extract()[0]
            fatalities = tr.xpath('td[5]/text()').extract()
            if fatalities:
                try:
                    if '+' in fatalities[0]:
                        fs = eval(fatalities[0])
                    else:
                        fs = int(fatalities[0])
                    if fs > 40:
                        yield scrapy.Request("http://aviation-safety.net"+link,
                                             callback=self._record_parse,
                                             meta={'fatalities': str(fs)})
                except ValueError as e:
                    print str(e)
            else:
                print "Unknown fatalities"

    def _record_parse(self, response):
        fval = '//div[@class="innertube"]/table//tr[{0}]/td[2]{1}/text()'

        l = ItemLoader(item=AviationItem(), response=response)
        l.add_xpath('date', fval.format(2, ""))
        l.add_xpath('time', fval.format(3, ""))
        l.add_xpath('operator', fval.format(5, "/a"))
        l.add_xpath('flight_number', fval.format(20, ""))
        l.add_value('fatalities', response.meta['fatalities'])
        l.add_xpath('departure', fval.format(18, "/"))
        l.add_xpath('destination', fval.format(19, "/"))
        l.add_xpath('crash', fval.format(15, "/"))
        yield l.load_item()
