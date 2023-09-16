import time
from confest import *
from page_objects.sms_encoder_elements import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
import allure


@allure.title("Sms Encoder")
class TestSmsEncoder:

    @pytest.fixture(scope="class", autouse=True)
    def visit_url(self, driver):
        driver.get(sms_encoder)
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.ID, "txtUserData"))
        )

    sms_list = [["Hello World", "+18984648186", "Default Alphabet - 7 Bits", 1],
                ["你好世界", "+18984648186", "Unicode - 16 Bits", 1],
                ["This is a GSM 8-bit message.", "+18984648186", "ANSI - 8 Bits", 1],
                ["Selenium provides extensions to emulate user interaction with browsers, a distribution server "
                 "for scaling browser allocation, and the infrastructure for implementations of the W3C WebDriver "
                 "specification that lets you write interchangeable code for all major web browsers.",
                 "+18984648186", "Default Alphabet - 7 Bits", 2]]

    @pytest.mark.parametrize("msg,number,encoding,seg", sms_list)
    def test_sms_pdu_encode(self, driver, msg, number, encoding, seg):
        allure.dynamic.title(f"Generate encoded SMS PDU!")
        driver.find_element(By.ID, "txtUserData").clear()
        driver.find_element(By.ID, "txtUserData").send_keys(msg)
        driver.find_element(By.ID, "txtPduDestinationNumber").clear()
        driver.find_element(By.ID, "txtPduDestinationNumber").send_keys(number)
        Select(driver.find_element(By.ID, "cboPduEncoding")).select_by_value(encoding)
        driver.find_element(By.ID, "TxtVP").clear()
        driver.find_element(By.ID, "TxtVP").send_keys("0")
        driver.find_element(By.ID, "BtnDecode").click()
        time.sleep(2)
        encoded_pdu = driver.find_element(By.ID, "TxtResult").text
        encoded_pdu = encoded_pdu.split("\n")
        sms_pdu = []
        if seg == 1:
            sms_pdu.append(encoded_pdu[1])
        elif seg == 2:
            sms_pdu.append(encoded_pdu[1])
            sms_pdu.append(encoded_pdu[4])
        allure.attach(f"Encoded PDU  --> {sms_pdu}", "output")
