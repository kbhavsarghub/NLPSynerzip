#5. Collect the first 15 articles from mashable feed, strip the html
# content of each of the 15 articles and create a plain text corpus from the same
import feedparser
from bs4 import BeautifulSoup

#Retreive the feed
myFeed = feedparser.parse("http://feeds.mashable.com/Mashable")
#Feed title
print('Feed Title :', myFeed['feed']['title'])

#Number of posts

post = myFeed.entries[0];
print('Number of posts :', len(myFeed.entries))
content = post.content[0].value
print('Raw content :\n',content)
soup = BeautifulSoup(content, 'html.parser')

#HTML Stripped text
print('Full text HTML Stripped:')
print(soup.get_text())