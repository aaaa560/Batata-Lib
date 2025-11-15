from batata.scraper import Scraper

# 1. Scraper básico
s = Scraper("https://quotes.toscrape.com")
print(s.get_title())
print(s.get_links()[:5])

# 2. Extração estruturada
schema = {
    "texto": "span.text",
    "autor": "small.author"
}
quotes = s.extract_list_structured("div.quote", schema)
print(quotes[0])

# 3. Tabelas
s2 = Scraper("https://www.scrapethissite.com/pages/forms/")
tabela = s2.get_table()
print(tabela[:3])