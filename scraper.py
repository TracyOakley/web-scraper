import requests
from bs4 import BeautifulSoup



#url =
#r =requests.get(url)
#print(r.text)
#markup = r.text
#why to use beautiful soup

#soup = BeautifulSoup(markup, "html.parser")
# beautiful soup want some markuop(r.text)

#the above is for parsing
# below will be for navigating

#playwright.dev/python/

def get_citations_needed_count(markup):
    #takes in a url string and returns an integer
    soup = BeautifulSoup(markup, "html.parser")

    citations = soup.find_all(title="Wikipedia:Citation needed")

    # Note from class: with requests need to check if "Python" in course.h1.text:
    # this is needed at because of the "invisible" text coming through
    # with Playwright this isn't an issue
    count = len(citations)

    return count

def get_citations_needed_report(markup):

    soup = BeautifulSoup(markup, "html.parser")
    citations = soup.find_all(title="Wikipedia:Citation needed")
    citations_print = "Citations from Wiki - History of Argentina" + "\n" + "\n"

    for cit in citations:

        citations_print += cit.find_parent("p").text + "\n"
        citations_print += "\n"

    return citations_print

if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/History_of_Argentina"
    response = requests.get(url)
    results = get_citations_needed_count(response.text)
    print("\n")
    print(results)
    print("\n")
    cit_print = get_citations_needed_report(response.text)
    print(cit_print)
