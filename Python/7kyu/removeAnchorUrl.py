
def remove_url_anchor(url):
    if '#' in url:
        return url[:url.index('#')]
    
    return url

print(remove_url_anchor("www.codewars.com#about"))
print(remove_url_anchor("www.codewars.com?page=1"))

# Complete the function/method so that it returns the url with anything after the anchor (#) removed.

# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"

# ALTERNATIVE METHOD

def remove_url_anchor2(url):

    return url.split('#')[0]