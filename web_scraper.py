
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def get_driver():
    # initialize options
    options = webdriver.ChromeOptions()
    # pass in headless argument to options
    options.add_argument('--headless')
    # initialize driver
    driver = webdriver.Chrome(chrome_options=options)
    return driver

def connect_to_base(browser, aa_sequence, aa_id):
    base_url = f"http://home.stagleys.co.uk/abysis/sequence_input/key_annotation/key_annotation.cgi?aa_sequence={aa_sequence}&nuc_sequence=&translation=sixft&humanorganism=on"
    connection_attempts = 0
    while connection_attempts < 10:
        try:
            browser.get(base_url)
            # wait for analysing and data to load
            # before returning True
            WebDriverWait(browser,1200).until(EC.presence_of_element_located((By.ID, 'Kabat_row')))
            # extract the request ID from page
            idtag = browser.find_element_by_class_name('initialised').get_attribute('id')
            idnum = str(re.search('\d+', idtag).group())
            print(f"{aa_id} (Request ID {idnum} ) was successfully analysed, ready for data fetching", time.ctime())
            return True,idnum
        except Exception as ex:
            connection_attempts += 1
            print(f'Error connecting to {base_url}.')
            print(f'Attempt #{connection_attempts}.')
    return False,connection_attempts

# def connect_to_base(browser, aa_sequence):
#     base_url = f"http://home.stagleys.co.uk/abysis/sequence_input/key_annotation/key_annotation.cgi?aa_sequence={aa_sequence}&nuc_sequence=&translation=sixft&humanorganism=on"
#     browser.get(base_url)
#     # wait for analysing and data to load
#     # before returning True
#     WebDriverWait(browser, 600).until(EC.presence_of_element_located((By.ID, 'Kabat_row')))
#     # extract the request ID from page
#     idtag = browser.find_element_by_class_name('initialised').get_attribute('id')
#     idnum = str(re.search('\d+', idtag).group())
#     print(f"Request ID {idnum} was successfully analysed, ready for data fetching", time.ctime())
#     return True, idnum



def write_to_file(output_df, filename, FILEDIR):

    df = pd.DataFrame(output_df)
    df.to_csv(f'{FILEDIR}//data//{filename}.csv',index=False)
    print(f"csv file saved as {FILEDIR}//data//{filename}.csv", time.ctime())