import scrapy

class ProductSpider(scrapy.Spider):
    name = 'test'
    start_urls = [
        'https://motokinisi.gr/gr/krani/full-face.html'
    ]

    def parse(self, response):
        # Извлича всички връзки на продуктите от началната страница
        product_links = response.xpath('//a[contains(@href, "/gr/kranos-")]/@href').getall()

        for link in product_links:
            # Преобразува относителния URL в абсолютен
            absolute_link = response.urljoin(link)
            yield response.follow(absolute_link, self.parse_product)

        # Следва линкове на следващите страници, ако има такива
        next_page = response.xpath('//a[contains(@class, "next")]/@href').get()
        if next_page:
            absolute_next_page = response.urljoin(next_page)
            yield response.follow(absolute_next_page, self.parse)

    def parse_product(self, response):
        self.logger.info(f'URL: {response.url}')
        if response.status == 200:
            self.logger.info('Page successfully loaded.')

            # Пробвай различни XPath селектори в зависимост от съдържанието на страницата

            # Опитай с различен XPath за името на продукта
            product_name = response.xpath('/html/body/div[3]/div[1]/div[1]/ul/li[5]/span/text()').get()
            if not product_name:
                product_name = response.xpath('/html/body/div[3]/div[1]/div[1]/ul/li[4]/span/text()').get()

            if product_name:
                product_name = product_name.strip()

            # Извличане на нова и стара цена
            new_price = response.xpath('/html/body/div[3]/div[1]/div[3]/div/div[2]/div[3]/div/span[1]/span/span/span/text()').get()
            old_price = response.xpath('/html/body/div[3]/div[1]/div[3]/div/div[2]/div[3]/div/span[2]/span/span/span/text()').get()

            # Проверка на друга структура за цената, ако е налична
            if not new_price:
                new_price = response.xpath('//div[contains(@class, "new-price")]/text()').get()
            if not old_price:
                old_price = response.xpath('//div[contains(@class, "old-price")]/text()').get()

            # Извличане на допълнителна информация
            additional_info = response.xpath('//div[contains(@class, "product-info")]/div[2]/div/div[2]/text()').get()
            if additional_info:
                additional_info = additional_info.strip()

            yield {
                'product_name': product_name,
                'old_price': old_price,
                'new_price': new_price,
                'additional_info': additional_info,
                'product_url': response.url,
            }
        else:
            self.logger.error(f'Failed to load page: {response.url} Status: {response.status}')
