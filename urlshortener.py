import pyshorteners
#TinyURL shortener service
def urlshort(url):
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(url)
    return short_url
