# Scrapy settings for moto_test project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "moto_test"

SPIDER_MODULES = ["moto_test.spiders"]
NEWSPIDER_MODULE = "moto_test.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "moto_test (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # За да игнорираш правила от robots.txt

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 2  # Забавяне от 2 секунди между заявките

# Enable or disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Enable or disable spider middlewares
#SPIDER_MIDDLEWARES = {
#    "moto_test.middlewares.MotoTestSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1,
}

# Proxy settings
HTTP_PROXY = 'http://dpDemo:wIGaE5hn4+5j1yyGyw@gr.smartproxy.com:30000'

# Enable or disable extensions
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
#ITEM_PIPELINES = {
#    "moto_test.pipelines.MotoTestPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
#AUTOTHROTTLE_ENABLED = True
#AUTOTHROTTLE_START_DELAY = 5
#AUTOTHROTTLE_MAX_DELAY = 60
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
