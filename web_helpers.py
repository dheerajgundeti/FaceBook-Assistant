
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def set_options():
    # adding options to allow permissions on pop ups
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-minimized")
    option.add_argument("--disable-extensions")
    # 1 for allow, 2 for blocking!!
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
    return option


def wait_till_pageloads(browser,identityby,value):
    delay=20 #seconds
    WebDriverWait(browser, delay).until(EC.presence_of_element_located((identityby, value)))