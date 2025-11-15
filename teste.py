from batata import Scraper

# 1. Scraper básico
s = Scraper("https://quotes.toscrape.com")
print(s.get_title())
print(s.get_links()[:15])
