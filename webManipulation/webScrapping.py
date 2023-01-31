import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
html = urlopen(url).read().decode('utf-8')
# print(html)

# scrapping the head of the page above and grabbing the title

lower_index, high_index = html.find('<head>') + len('<head>'), html.find(
    '</head>')
print(html[lower_index: high_index])

# using regular exp

pattern = '<head.*?>.*?</head.*?>'
match_results = re.search(pattern, html, re.IGNORECASE)
# head_properties = match_results.group()
# matched_results = re.sub('<.*?>', '', head_properties)
# print(matched_results)
