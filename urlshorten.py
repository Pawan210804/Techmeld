import pyshorteners

# Function to shorten the URL
def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return s.tinyurl.short(url)

# Take input from user
url = input("Enter the URL: ")
shortened = shorten_url(url)

print("Shortened URL:", shortened)


