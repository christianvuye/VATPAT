from selenium import webdriver

def test_initial_page_title():
    browser = webdriver.Firefox()
    browser.get("http://localhost:8000")
    assert "Dashboard" in browser.title
    browser.quit()  # Don't forget to close the browser to clean up