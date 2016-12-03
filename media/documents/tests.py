from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import LiveServerTestCase

class SearchTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def getURL(self, namespace):
        return "http://127.0.0.1:8000" + reverse(namespace)

    def testsearchbar(self):
        self.browser.get(self.getURL(("")))
        elem = self.browser.find_element_by_name("query")
        elem.send_keys("task")
        elem.submit()
        self.assertHTMLEqual(self.browser.current_url, self.getURL("search") + "?query=task")
        rows = self.browser.find_elements_by_class_name("row")
        for r in rows:
            self.assertIn("task", r.text)