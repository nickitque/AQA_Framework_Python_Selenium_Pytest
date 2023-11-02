class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # Define methods for interacting with elements on the home page
    def search_for_product(self, product_name):
        search_box = self.driver.find_element_by_id("search-box")
        search_box.clear()
        search_box.send_keys(product_name)
        search_box.submit()
