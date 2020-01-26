import requests
import re

followers_translations = "|".join([
    "Abonnés",
    "Followers"
])

def extract_twitter_followers(url_input):
    r = requests.get('https://twitter.com/KMbappe')
    # We try to match 3\u202f800\u202f668 Abonnés
    space_unicode = "\u202f"
    regex = f"[0-9{space_unicode}{{0,1}}]+ ({followers_translations})"
    # Can't use data-count because there are many other data-count, and also the regex won't find text between Abonnés and data-count if there is a break between
    # regex2 = "Abonnés.*data-count"
    matched = re.search(regex, r.text).group()
    replace_unicode = re.sub(space_unicode, "", matched)
    extract_number = re.search("[0-9]+", replace_unicode).group()
    return int(extract_number)


url = "https://twitter.com/KMbappe"
n_followers = extract_twitter_followers(url)
print(f"for input {url}, we have {n_followers} followers")