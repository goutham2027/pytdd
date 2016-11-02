import os
import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        chromedriver = "/Users/gouthampilla/Downloads/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.browser = webdriver.Chrome(chromedriver)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        # self.fail("Finish the test!")


if __name__ == '__main__':
    unittest.main()

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. She enters
# "Use peacock feathers to make a fly"

# The page updates again, and now shows both items on her list

# There exists a unique URL for each of the to-do items
