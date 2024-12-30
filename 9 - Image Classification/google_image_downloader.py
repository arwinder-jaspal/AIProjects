from icrawler.builtin import GoogleImageCrawler

search_name = "Joker"
crawler = GoogleImageCrawler(storage={'root_dir': '9 - Image Classification/dataset/' + search_name})
crawler.crawl(keyword=search_name, max_num=20) 

