import pytest
from selenium import webdriver
# browsers = ["Edge", "Chrome"]
browsers = ["Edge"]


@pytest.fixture(scope="session", autouse=True, params=browsers)
def driver(request):
    browser = request.param
    driver = None
    if browser == "Edge":
        driver = webdriver.Edge()
    elif browser == "Chrome":
        driver = webdriver.Chrome()
    else:
        assert False, f"{browser} is not supported!!"
    print(f"Opening {browser} browser!!!")
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()
