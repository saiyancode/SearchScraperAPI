from lxml import html as lh
from bs4 import BeautifulSoup
import tldextract

def parse_html(html):
    results = []
    lxml_doc = lh.fromstring(html)
    organic_blocks = lxml_doc.cssselect('div.g')
    paid_blocks = lxml_doc.cssselect('li.ads-ad')
    rank = 1
    for res in organic_blocks[:-1]:
        result = organic_attributes(res)
        if result:
            result.update({'rank': rank, 'type': 'organic'})
            results.append(result)
            rank += 1

    rank = 1
    for res in paid_blocks:
        result = paid_attributes(res)
        if result:
            result.update({'rank': rank, 'type': 'paid'})
            results.append(result)
            rank += 1

    return results

def paid_attributes(block):
    html = lh.tostring(block).decode('utf-8', errors='ignore')
    soup = BeautifulSoup(html, 'lxml')

    domain = soup.find('cite', attrs={'class': 'UdQCqe'})
    url = soup.find('cite', attrs={'class': 'UdQCqe'})
    if url:
        domain = tldextract.extract(domain.text).domain + "." + tldextract.extract(domain.text).suffix
        url = url.text
    # This stores all the paid position data
    title = soup.find('h3')
    if title:
        title = title.text

    return {'url': url, 'domain':domain,'title': title}

def organic_attributes(result_block):
    html = lh.tostring(result_block).decode('utf-8', errors='ignore')
    soup = BeautifulSoup(html, 'lxml')

    link = soup.find('a', href=True)
    if link:
        link = link['href']
        domain = tldextract.extract(link).domain + "." + tldextract.extract(link).suffix

    title = soup.find('h3', {'class':'r'})
    if title:
        title = title.get_text()

    description = soup.find('span', {'class':'st'})
    if description:
        description = description.get_text()

    reviews = soup.find('div', attrs={'class': 'slp f'})
    if reviews:
        reviews = True
    else:
        reviews = soup.find('div', attrs={'class': 'f slp'})
        if reviews:
            reviews = True
        else:
            reviews = False

    if link.startswith('/') or link.startswith('#'):
        return

    
    return {'url': link, 'domain': domain, 'title': title, 'description': description, 'reviews':reviews}