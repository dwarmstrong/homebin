#!/usr/bin/env python3
# Inspired by "Automate the Boring Stuff with Python" / by Al Sweigart
from bernersLee import Browser

msg = """
(O< .: Get book information from command line arguments or clipboard and open
(/)_   web browser and search Amazon and the Toronto Public Library.
"""

def main():
    library = "https://www.torontopubliclibrary.ca/search.jsp?Ntt="
    amazonCa = "https://www.amazon.ca/s/ref=nb_sb_noss_1?"
    amazonCom = "https://www.amazon.com/s/ref=nb_sb_noss_1?"
    amzSearch = "url=search-alias%3Dstripbooks&field-keywords="

    browser = Browser()
    browser.open_search_tab(library)
    browser.open_search_tab(amazonCa + amzSearch)
    browser.open_search_tab(amazonCom + amzSearch)

main()
