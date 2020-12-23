"""
These tests cover DuckDuckGo searches
"""
import pytest
from pages.result import DuckDuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bar'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckDuckGoResultPage(browser)

    #Given the DuckDuckGo home page is displayed
    search_page.load()

    #When the user searches for "panda"
    search_page.search(phrase)
   
    #Then the search result query is "panda"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

     
    #And the search result title contains "panda"
    assert phrase in result_page.title()
