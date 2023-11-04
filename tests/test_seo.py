from pages.seo_page import RobotsAndSitemapPage

robots = "https://takservice.pl/robots.txt"
sitemap = "https://takservice.pl/sitemap_index.xml"


def test_presence_of_robots_text(browser):
    """Test for robots.txt file. It should contain User agent info, disallow, sitemap url etc."""
    page = RobotsAndSitemapPage(browser, robots)
    page.open()
    page.check_robots_txt_text()


def test_check_page_category_url(browser):
    """Test for presence of 'page' category url at 'sitemap_index.xml' endpoint"""
    page = RobotsAndSitemapPage(browser, sitemap)
    page.open()
    page.check_sitemap_xml_page_category_url()


def test_check_deals_category_url(browser):
    """Test for presence of 'deals' category url at 'sitemap_index.xml' endpoint"""
    page = RobotsAndSitemapPage(browser, sitemap)
    page.open()
    page.check_sitemap_xml_deals_category_url()


def test_check_page_category_urls(browser):
    """Test for presence of urls in 'page' category of sitemap."""
    page = RobotsAndSitemapPage(browser, sitemap)
    page.open()
    page.click_sitemap_xml_page_category_url()
    page.check_sitemap_xml_homepage_url()
    page.check_sitemap_xml_privacy_url()


def test_check_deals_category_urls(browser):
    """Test for presence of urls in 'deals' category of sitemap."""
    page = RobotsAndSitemapPage(browser, sitemap)
    page.open()
    page.click_sitemap_xml_deals_category_url()
    page.check_sitemap_xml_first_deal_url()
    page.check_sitemap_xml_second_deal_url()
    page.check_sitemap_xml_third_deal_url()
    page.check_sitemap_xml_fourth_deal_url()
