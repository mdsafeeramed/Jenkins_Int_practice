# pytest unittest framework we can execute testcases conditionally.
# in pytest framework(unittest) filename should start with test.
# Method (functions) should start with test name. (Note need to calls function it directly call if test name is specified
# All explanation is mentioned in single file.
# like @pytest decorators like mark, fixture, execution of the pytest commands.
# please refer udemy selenium course section pytest.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

@pytest.fixture(scope="module")
def setup_config():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    driver.close()

@pytest.mark.sanity
def test_tc_001(setup_config):
    driver.get("https://www.facebook.com")
    # assert means compare actually with expected results
    assert driver.title == "Facebook – log in or sign up"

# write multiple testcase in same file.

@pytest.mark.smoke
def test_tc_002(setup_config):
    driver.get("https://www.facebook.com")
    assert driver.current_url == "https://www.facebook.com/"


@pytest.mark.sanity
def test_tc_003(setup_config):
    driver.get("https://accounts.google.com/signup")
    assert driver.title == "Sign in – Google accounts"


@pytest.mark.testcase4
def test_tc_004(setup_config):
    driver.get("https://accounts.google.com/signup")
    driver.find_element(By.NAME, "firstName").send_keys("testing")
    driver.find_element(By.XPATH, "//button[@type='button']").click()
    # using webdriver wait until ID is found
    driver.set_page_load_timeout(40)
    # implict wait
    # driver.implicitly_wait(40)
    time.sleep(10)
    #element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'month'),"April"))
    driver.find_element(By.XPATH, "//*[@id='month']").click()
    objc = Select(driver.find_element(By.XPATH, "//select[@class='UDCCJb']"))
    objc.select_by_visible_text("April")
    time.sleep(10)
    assert objc.first_selected_option.text == "April"



