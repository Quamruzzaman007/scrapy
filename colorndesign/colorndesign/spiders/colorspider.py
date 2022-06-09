from gc import callbacks
from re import S
from unicodedata import name
from itemloaders import ItemLoader
import scrapy
from colorndesign.items import ColorndesignItem

class ColorNDesign(scrapy.Spider):
    name = "colorndesign"
    start_urls = ["https://colouranddesign.com/digital/photo-gallery"]


    def parse(self, response):
        category = response.xpath("//div[@class='esg-media-cover-wrapper']/div[2]")
        base ="https://colouranddesign.com"
        for c in category:
            url =  c.css("div")[2].css("a,galleryLink").attrib['href']
        #products-grid > li:nth-child(1) > div.product_after_shop_loop > div > div.product_after_shop_loop_buttons > div.colorName
            yield response.follow(base + url, callback =  self.parse_categories)
    

    def parse_categories(self, response):
        products = response.xpath("//*[@id='products-grid']/li")
        for product in products:
            
            
            name_css='h3  a::text'
            Sku_css='div.productSKU::text'
            color_css='div.colorName::text'
            Breadcrumbs_xpath='//*[@id="content"]/div/div[3]/div[1]/div/div/div[1]/nav/span//following-sibling::text()'
            Product_Url_css='h3 a::attr(href)'

            l = ItemLoader(item = ColorndesignItem(),
                            selector=product)

            l.add_css('name', name_css)
            l.add_css('Sku', Sku_css)
            l.add_css('color', color_css)
            l.add_xpath('Breadcrumbs', Breadcrumbs_xpath)
            l.add_css('Product_Url', Product_Url_css)

            item = l.load_item()
            
            yield item

            # item = ColorndesignItem()

            # item["name"] = product.css(name_css).get()
            # item["Sku"] = product.xpath(Sku_xpath).get()
            # item["color"] = product.xpath(colo_xpath).get()
            # item["Breadcrumbs"] = response.xpath(Breadcrumbs_xpath).get()
            # item["Product_Url"] = product.css(Product_Url_css).get()

            # yield item
            
