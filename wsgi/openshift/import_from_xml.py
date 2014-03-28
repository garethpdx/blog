import codecs
import datetime
import bs4


def get_articles():
	with codecs.open(r'C:\Users\gareth\Downloads\blog-03-25-2014.xml','r','utf-8') as f:
		r = bs4.BeautifulSoup(f.read())
		
	for entry in r.find_all('entry'):
		for category in entry.find_all('category'):		
			if category.attrs['term'] <> 'http://schemas.google.com/blogger/2008/kind#post':
				# this is not a post
				continue
			content, title, published_date, draft = parse_post(entry)
			if draft:
				title = 'DRAFT - %s' % title
			yield {'title': title, 'contents': content, 'published_date': published_date}			

if __name__ == '__main__':			
	for x in getArticles():
		print x['published_date']
		
def parse_post(entry):		
	contents = entry.find_all('content')[0].text	
	title = entry.find_all('title')[0].text.replace('?','').replace('/',' or ')
	published = entry.find_all('published')[0].text
	published_date = datetime.date(int(published[:4]),int(published[5:7]), int(published[8:10]))
	draft = entry.find_all('app:draft')
	return contents, title, published_date, draft