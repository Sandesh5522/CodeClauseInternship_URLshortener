import pyshorteners
long_url = input("Enter the URL to shorten: ")

#TinyURL shortener service
def urlshort(url):
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(url)
    return short_url

short_url = urlshort(long_url)
print("The Shortened URL is: " + short_url)
