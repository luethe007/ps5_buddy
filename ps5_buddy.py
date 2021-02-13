from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from twilio.rest import Client
from datetime import datetime

client = Client()
driver = webdriver.Chrome(ChromeDriverManager().install())


def clear_cache(driver):
    """Clear the cookies and cache for the ChromeDriver instance."""
    # navigate to the settings page
    driver.get('chrome://settings/clearBrowserData')
    time.sleep(4)
    # click the button to clear the cache
    clearButton = driver.execute_script("return document.querySelector('settings-ui') \
        .shadowRoot.querySelector('settings-main').shadowRoot.querySelector('settings-basic-page') \
        .shadowRoot.querySelector('settings-section > settings-privacy-page').shadowRoot.querySelector \
        ('settings-clear-browsing-data-dialog').shadowRoot.querySelector('#clearBrowsingDataDialog') \
        .querySelector('#clearBrowsingDataConfirm')")
    clearButton.click()
    time.sleep(10)

def main():
    """Go on amazon and check if PS5 is available, then clear cache and do it again."""
    i=0
    time_store = set()
    # keep looping between amazon and browser clear_cache
    while True:
        now = datetime.now()
        now_tuple = (now.hour, now.minute)
        # send confirmation
        if (now_tuple not in time_store) and (now_tuple[1] == 0):
            time_store.add(now_tuple)
            client.messages.create(body='Läuft!!!',
              from_=os.environ["FROM_WHATSAPP_NUMBER"],
              to=os.environ["TO_WHATSAPP_NUMBER"])

        # go on amazon
        driver.get('https://www.amazon.de/Sony-Interactive-Entertainment-PlayStation-5/dp/B08H98GVK8/ref=sr_ \
            1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=ps5&qid=1606155052&sr=8-1&th=1')
        time.sleep(4)

        # accept cookies
        try:
            driver.find_element_by_xpath('//*[@id="sp-cc-accept"]').click()

        except:
            print('Cookies already accepted.')    
        time.sleep(4)
        
        # click on ps5 digital edition
        try:
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div[5]/div[4]/div[30]/div[1]/div/form/div/ul/li[7]/span/div/span/span/span/button/div/div[1]/span').click()
        except:
            print('Already on PS5 Digital Edition')
        time.sleep(4)

        # get availability
        availability = driver.find_element_by_xpath('//*[@id="availability"]/span').text
        
        # check availability and send whatsapp if PS5 is available
        if availability != 'Derzeit nicht verfügbar.':
            client.messages.create(body='PS5 kaufen!!!',
                            from_=os.environ["FROM_WHATSAPP_NUMBER"],
                            to=os.environ["TO_WHATSAPP_NUMBER"])
            os.system('play -nq -t alsa synth {} sine {}'.format(5, 440))
            print('PS5 kaufen!!!')
            break
        print(str(i),availability)
        clear_cache(driver)
        time.sleep(15)
        i+=1

if __name__ == '__main__':
    main()
