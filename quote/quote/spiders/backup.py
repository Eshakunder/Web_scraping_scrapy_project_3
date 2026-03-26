import scrapy

from ..items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    page_number = 2 #we will start from page 2 because we have already scraped the first page in the start_urls. we will follow the next page link until there is no next page. this is added for scraping websites with pagination.
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"] #list of url to scrape.


    def parse(self, response):
        item = QuoteItem() #create an instance of the QuoteItem class
        # title = response.css("title").extract() #extract title
        # yield {"title": title} #yield the title as a dictionary
        all_div_quotes = response.css("div.quote")#we want all the div with class quote
        for quotes in all_div_quotes:
          title = quotes.css('span.text::text').extract()
        #extract the title of the span class 
          author = quotes.css('small.author::text').extract()
        #extract the author of the small class
          tags = quotes.css('.tag::text').extract()

          item['title'] = title
          item['author'] = author
          item['tags'] = tags
          yield item
        #   yield{"title": title,
        #       "author": author,
        #       "tags": tags
        # }
        #the below code is for scraping multiple pages. we will extract the next page link and follow it until there is no next page.
        # next_page = response.css('li.next a::attr(href)').get() #extract the next page link
        # if next_page is not None: #do untill there is a next page . if next page is not none then follow the next page link and call the parse function again to extract the data from the next page.
        #     yield response.follow(next_page, callback=self.parse)
        #     #its like recursive method. it will call the parse function again and again until there is no next page.
 

        #scraping websites with pagination.
        next_page = 'https://quotes.toscrape.com/page/'+ str(QuotesSpider.page_number)+ '/'
        if QuotesSpider.page_number <= 11: #we have 10 pages to scrape. so we will scrape until page number is less than 11.
            QuotesSpider.page_number += 1 #increment the page number by 1
            yield response.follow(next_page, callback=self.parse) #follow the next page link and call the parse function again to extract the data from the next page.