#Bot to purchase an out of stock item from bestbuy

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from numpy import random
from time import sleep

if __name__ == "__main__":
    # Get driver from path
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = wd.Chrome(PATH)

    # Get information from a text file
    info_file = open("buy_info.txt")
    email = info_file.readline().strip()
    pwd = info_file.readline().strip()
    first = info_file.readline().strip()
    last = info_file.readline().strip()
    addr = info_file.readline().strip()
    city = info_file.readline().strip()
    state = info_file.readline().strip()
    zip = info_file.readline().strip()
    cc = info_file.readline().strip()
    exp_mo = info_file.readline().strip()
    exp_yr = info_file.readline().strip()
    sc = info_file.readline().strip()
    info_file.close()

    # Go to the desired bestbuy URL
    URL = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
    driver.get(URL)

    # Refresh the page until the sold-out button is gone and the item
    # can be added to cart
    while True:
        add_to_cart = driver.find_element(By.XPATH, "//div[@class='fulfillment-add-to-cart-button']")
        sold_out_button = driver.find_element(By.XPATH, "//div[@class='fulfillment-add-to-cart-button']/div/div/button")
        sold_out_text = sold_out_button.get_attribute("class")
        if "disabled" not in sold_out_text:
            break
        sleep(random.randint(5, 10))
        driver.refresh()

    # Conduct all of the operations to purchase the item
    add_to_cart.click()

    go_to_cart = driver.find_element(By.XPATH, "//a[@data-lid='hdr_carticon']")
    go_to_cart.click()

    checkout_button = WebDriverWait(driver, 60).until(
        ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-lg btn-block btn-primary']"))
    )
    checkout_button.click()

    email_input = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    email_input.send_keys(email)

    pass_input = driver.find_element(By.XPATH, "//input[@type='password']")
    pass_input.send_keys(pwd)

    sign_in = driver.find_element(By.XPATH, "//button[@type='submit']")
    sign_in.click()

    first_name_input = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "//input[@id='firstName']"))
    )
    first_name_input.send_keys(first)

    last_name_input = driver.find_element(By.XPATH, "//input[@id='lastName']")
    last_name_input.send_keys(last)

    address_input = driver.find_element(By.XPATH, "//input[@id='street']")
    address_input.send_keys(addr)

    city_input = driver.find_element(By.XPATH, "//input[@id='city']")
    city_input.send_keys(city)

    zip_input = driver.find_element(By.XPATH, "//input[@id='zipcode']")
    zip_input.send_keys(zip)

    state_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='state']"))
    state_dropdown.select_by_value(state)

    continue_payment_button = driver.find_element(By.XPATH, "//button[@class='btn btn-lg btn-block btn-secondary']")
    continue_payment_button.click()

    cc_input = WebDriverWait(driver, 30).until(
        ec.presence_of_element_located((By.XPATH, "//input[@id='optimized-cc-card-number']"))
    )
    cc_input.send_keys(cc)

    exp_mo_dropdown = Select(driver.find_element(By.XPATH, "//select[@name='expiration-month']"))
    exp_mo_dropdown.select_by_value(exp_mo)

    exp_yr_dropdown = Select(driver.find_element(By.XPATH, "//select[@name='expiration-year']"))
    exp_yr_dropdown.select_by_value(exp_yr)

    sc_input = driver.find_element(By.XPATH, "//input[@id='credit-card-cvv']")
    sc_input.send_keys(sc)

    # Leaving buying button out of this version

    # Quit out of the driver
    driver.quit()
