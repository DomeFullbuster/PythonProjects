import  unittest
from selenium import webdriver

class SearchText(unittest.TestCase):
    def setUp(self):
        #create a new Firefox session

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        #navigate to the application home page

        self.driver.get("http://www.google.com?")

    def test_search_by_text(self):
        #get the search textbox

        self.search_field = self.driver.find_element_by_name("q")

        #enter search keyword and submit

        self.search_field.send_keys("Selenium Webdriver Interview questions")
        self.search_field.submit()

        #get the list of elements which are displayed after the search
        #currently on result page usingfind_elements_by_class_namemethod

        lists = self.driver.find_elements_by_name("r")
        no=len(lists)
        self.assertEquals(10, len(lists))

    def tearDown(self):

        #close the browser window

        self.driver.quit()

