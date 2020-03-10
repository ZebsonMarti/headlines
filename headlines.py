from flask import Flask
import feedparser

app = Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/")
def get_news():
    feed = feedparser.parse(BBC_FEED)
    first_article = feed['entries'][0]
    return """
        <html>
            <body>
                <h1> BBC headlines </h1>
                <b>{0}</b> <br/>
                <i>{1}</b> <br/>
                <p>{2}</p>
            </body>
        </html>
    """.format(first_article.get('title'),first_article.get('published'),first_article.get('summary'))


if __name__ == "__main__":
    app.run(port=5000, debug=True)
