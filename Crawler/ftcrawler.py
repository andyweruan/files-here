import urllib2

def fetch_html(url):
    html = urllib2.urlopen(url).read()
    return html

def get_title(html):
    title_start = html.find('<title>')
    title_end = html.find('</title>', title_start)
    title = html[title_start + 7: title_end]
    return title

def get_links(html):
    i = 0
    link_start = title_start = html.find('<li><a href=', i)
    link_end = html.find('\"', link_start + 14)
    link = html[link_start + 13: link_end]
    i = link_end + 1
    return link
urls = [
    'https://en.wikipedia.org/wiki/Main_Page'
]
#for url in urls:
#    html = fetch_html(url)
#    print get_title(html)
for url in urls:
    while True
        html = fetch_html(url)
        link = get_links(html)
        print link
#    if link.find("wikipedia.org") == -1:
#        link = 'https://en.wikipedia.org' + link
#    urls.append(link)
#    urls.append(get_links(html))
