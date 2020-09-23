from requests_html import HTML, HTMLSession

# path = 'https://www.newegg.com/global/ph-en/p/pl?d=x570' 
# path_1 = 'https://www.lazada.com.ph/catalog/?spm=a2o4l.home.search.3.4107359dZNdpAW&q=2080%20ti&_keyori=ss&from=search_history&sugg=2080%20ti_2_1'
path_2 = 'https://www.github.com/search?q=python'
path_3 = 'https://www.ebay.ph/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=2080ti&_sacat=0'
path_4 = 'https://www.lazada.com.ph/shop-plants-seeds/'
path_5 = 'https://www.lazada.com.ph/'
path_6 = 'https://www.python.org/'

session = HTMLSession()
r = session.get(path_5).html

r.render()
print(r.text)
#match = r.find('div.c5TXIP')
#print(match[0].text)


# print(r.html)
# match = r.find('title')[0]

# match_div = r.find('div.item-cell')
# print(match_div[0].text)
# print(match_div)
# entry = match_div[0]

#item_title = entry.find('a.item-title', first=True)
#item_name = item_title.text
#print(item_name)

#item_price = entry.find('div.item-action', first=True)
#print(item_price.text)
#print(entry.text)
