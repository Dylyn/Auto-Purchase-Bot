import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import info

# disable bot detection on chrome/BestBuy
options = Options()
#Options.add_argument('--disable-blink-features=AutomationControlled')

# for using the browser
browser = webdriver.Chrome('C:\webdrivers\chromedriver.exe',options=options)

# Test Product
PS5Controller = 'https://www.bestbuy.ca/en-ca/product/playstation-5-dualsense-wireless-controller-white/14962193'
rtx3080TI = 'https://www.bestbuy.ca/en-ca/product/asus-rog-strix-nvidia-geforce-rtx-3080-ti-oc-12gb-gddr6x-video-card/15493494'
rtx30870TI = 'https://www.bestbuy.ca/en-ca/product/msi-nvidia-geforce-rtx-3070-ti-ventus-3x-oc-8gb-gddr6x-video-card/15547753'

# website page
browser.get(rtx3080TI)

completeCheck = False

while not completeCheck: 
    try:
        # wait for item page to load
        foundButton = False
        while not foundButton:
            
            addToCartBtn = addButton = browser.find_element_by_class_name('button_2m0Gt')

            if ("disabled_LqxUL" in addToCartBtn.get_attribute("class")):
                # delay before refresh (sec)
                time.sleep(2)

                # refresh page
                browser.refresh()

            else:
                foundButton = True

        # add to cart
        print("add to cart")
        addToCartBtn.click()

        # wait for item to be added to cart
        foundButton = False
        while not foundButton:

            checkoutBtn = addButton = browser.find_element_by_class_name('button_E6SE9')

            if ("secondary_2Lchg" in checkoutBtn.get_attribute("class")):
                # delay for page to load (sec)
                time.sleep(1)

            else:
                foundButton = True

        # go to cart
        time.sleep(2)
        print("going to cart")    
        browser.get("https://www.bestbuy.ca/en-ca/basket")

        # click checkout button
        time.sleep(1)
        checkoutBtn = addButton = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div/section/div/main/section/section[2]/div[2]/div/a")
        print("continue checkout")
        checkoutBtn.click()

        # click checkout as guest
        time.sleep(1)
        guestCheckoutBtn = addButton = browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div[2]/a")
        print("checking out as guest")
        guestCheckoutBtn.click()

        # autofill personal information
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='email']").send_keys(info.email)
        browser.find_element(By.XPATH,"//*[@id='firstName']").send_keys(info.first_name)
        browser.find_element(By.XPATH,"//*[@id='lastName']").send_keys(info.last_name)
        browser.find_element(By.XPATH,'//*[@id="addressLine"]').send_keys(info.address)
        browser.find_element(By.XPATH,'//*[@id="city"]').send_keys(info.city)
        browser.find_element(By.XPATH,'//*[@id="regionCode"]').send_keys(info.region_code)
        browser.find_element(By.XPATH,'//*[@id="postalCode"]').send_keys(info.postal_code)
        browser.find_element(By.XPATH,'//*[@id="phone"]').send_keys(info.phone)

        # confirm personal information
        confirmShippingBtn = addButton = browser.find_element_by_xpath("/html/body/div[1]/form/div/div/div/section[2]/main/div[2]/section/section[1]/button")
        print("confirmed shipping")
        confirmShippingBtn.click()

        # fill payment method
        time.sleep(2)
        browser.find_element(By.XPATH,'//*[@id="shownCardNumber"]').send_keys(info.card_number)
        browser.find_element(By.XPATH,'//*[@id="expirationMonth"]').send_keys(info.month)
        browser.find_element(By.XPATH,'//*[@id="expirationYear"]').send_keys(info.year)
        browser.find_element(By.XPATH,'//*[@id="cvv"]').send_keys(info.cvv)

        confirmPayMethod= addButton = browser.find_element_by_xpath("/html/body/div[1]/div[5]/div/div/section[2]/main/div[2]/section/section[1]/button")
        print("confirmed payement method")
        confirmPayMethod.click()

        completeCheck = True
    except:
        # restart bot if error occurs in process
        print("error - restarting")
        print("")
        browser.get(rtx3080TI)




# disabled button:
# class="button_2m0Gt primary_RXOwf addToCartButton_1op0t addToCartButton regular_23pTm disabled_LqxUL" <<<<< notice 'disabled_LqxUL'

# enabled button
# class="button_2m0Gt primary_RXOwf addToCartButton_1op0t addToCartButton regular_23pTm"

# BestBuy PS5: https://www.bestbuy.ca/en-ca/product/playstation-5-console/14962185
# BestBuy PS5 Controller (test): https://www.bestbuy.ca/en-ca/product/playstation-5-dualsense-wireless-controller-midnight-black/15480210