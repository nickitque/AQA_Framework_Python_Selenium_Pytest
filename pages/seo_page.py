from .locators import SeoPageLocators
from .base_page import BasePage


class RobotsAndSitemapPage(BasePage):
    def check_robots_txt_text(self):
        robots_text = self.browser.find_element(*SeoPageLocators.ROBOTS_TEXT).text
        one_line_robots_text = " ".join(line.strip() for line in robots_text.splitlines())
        assert one_line_robots_text == "# START YOAST BLOCK # --------------------------- " \
                                       "User-agent: * Disallow:  Sitemap: https://takservice.pl/sitemap_index.xml " \
                                       "# --------------------------- # END YOAST BLOCK"

    def check_sitemap_xml_page_category_url(self):
        page_category = self.browser.find_element(*SeoPageLocators.PAGE_CATEGORY)
        assert (page_category.get_attribute('href')) == "https://takservice.pl/page-sitemap.xml", \
            "The page category link is not https://takservice.pl/page-sitemap.xml"

    def check_sitemap_xml_deals_category_url(self):
        deals_category = self.browser.find_element(*SeoPageLocators.DEALS_CATEGORY)
        assert (deals_category.get_attribute('href')) == "https://takservice.pl/deals-sitemap.xml", \
            "The page category link is not https://takservice.pl/deals-sitemap.xml"

    def click_sitemap_xml_page_category_url(self):
        self.browser.find_element(*SeoPageLocators.PAGE_CATEGORY).click()

    def click_sitemap_xml_deals_category_url(self):
        self.browser.find_element(*SeoPageLocators.DEALS_CATEGORY).click()

    def check_sitemap_xml_homepage_url(self):
        deals_category = self.browser.find_element(*SeoPageLocators.HOMEPAGE_URL)
        print(deals_category.get_attribute('href'))
        assert (deals_category.get_attribute('href')) == "https://takservice.pl/ru/", \
            "The page category link is not https://takservice.pl/ru/"

    def check_sitemap_xml_privacy_url(self):
        deals_category = self.browser.find_element(*SeoPageLocators.DEALS_CATEGORY)
        assert (deals_category.get_attribute('href')) == "https://takservice.pl/ru/policy/", \
            "The page category link is not https://takservice.pl/ru/policy/"

    def check_sitemap_xml_first_deal_url(self):
        deals_category = self.browser.find_element(*SeoPageLocators.DEALS_TO15_URL)
        assert (deals_category.get_attribute('href')) == "https://takservice.pl/ru/deals/to15/", \
            "The page category link is not https://takservice.pl/ru/deals/to15/"

    def check_sitemap_xml_second_deal_url(self):
        deals_category = self.browser.find_element(*SeoPageLocators.DEALS_CHECK0ZL_URL)
        assert (deals_category.get_attribute('href')) == "https://takservice.pl/ru/deals/check0zl/", \
            "The page category link is not https://takservice.pl/ru/deals/check0zl/"

    def check_sitemap_xml_third_deal_url(self):
        deals_category = self.browser.find_element(*SeoPageLocators.DEALS_DIAGNOSTICS0ZL_URL)
        assert (deals_category.get_attribute('href')) == "https://takservice.pl/ru/deals/diagnostics0zl/", \
            "The page category link is not https://takservice.pl/ru/deals/diagnostics0zl/"

    def check_sitemap_xml_fourth_deal_url(self):
        deals_category = self.browser.find_element(*SeoPageLocators.DEALS_TAKCLUB_URL)
        assert (deals_category.get_attribute('href')) == "https://takservice.pl/ru/deals/takclub/", \
            "The page category link is not https://takservice.pl/ru/deals/takclub/"
