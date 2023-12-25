# Microsoft Account Generator
# IMPORTS
from os import close
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from discord.webhook import Webhook
import requests
import discord
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
import names
from os import replace
import names
import re
import random
import string



#USER INPUT
# See CSV to Python List to convert a profile spreadsheet to the desired format
# Profile Format: [[task number, first name, last name, card number, MM, YY, CVV, address line 1, address line 2, city, province, postal code, phone ][...][...]...]
ProfileRotation = []
#Insert Discord Webhook -> ""
webhook = DiscordWebhook(url="")
#Catchall Domain
Catchall = "example.ca"
#chromedriver.exe path (Must be replaced!)
chrome_options = Options()
PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
driver = webdriver.Chrome(PATH)


#Account Generation
# Adjust sleep times according to latency
for x in ProfileRotation:
    driver.get('https://login.live.com/logout.srf?ct=1632608934&rver=7.0.6738.0&lc=1033&id=292666&ru=https%3A%2F%2Faccount.microsoft.com%2Fauth%2Fcomplete-signout%3Fru%3Dhttps%253A%252F%252Faccount.microsoft.com%252Fbilling%252Faddresses')
    time.sleep(2)
    driver.get("https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&rver=7.3.6963.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.microsoft.com%2fen-ca%2fstore%2fcart%3flc%3d4105&id=74335&contextid=3DCC350762FF5378&bk=1635549714&uiflavor=web&lic=1&mkt=EN-CA&lc=4105&uaid=e27df93cce6a4360b4b67a788d31fdf4")
    
    
    
    #Email Name Generation
    def urlify(FirstLast):
        # Remove all non-word characters (everything except numbers and letters)
        FirstLast = re.sub(r"[^\w\s]", '', FirstLast)
        # Replace all runs of whitespace with a single dash
        FirstLast = re.sub(r"\s+", '_', FirstLast)
        return FirstLast
    

    # Creates email address using catchall domain
    FirstLast = urlify((names.get_first_name()))
    Name = (FirstLast+Catchall)
    # Password Generation
    # get random password pf length 8 with letters, digits, and symbols
    Characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(Characters) for i in range(11))


    #Enters User & Password
    EmailForm = driver.find_element_by_xpath('//*[@id="MemberName"]')
    EmailForm.click()
    EmailForm.send_keys(x[1]+Name)

    Next = driver.find_element_by_xpath('//*[@id="iSignupAction"]')
    Next.click()

    try:
        Pass = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="PasswordInput"]'))
        )
    finally: 
     PassForm = driver.find_element_by_xpath('//*[@id="PasswordInput"]')
    PassForm.click()
    PassForm.send_keys(password)

    ShowPass = driver.find_element_by_xpath('//*[@id="ShowHidePasswordCheckbox"]')
    ShowPass.click()

    Next1 = driver.find_element_by_xpath('//*[@id="iSignupAction"]')
    Next1.click()

    #Enters Full Name
    try:
        FLNameFields = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="FirstName"]'))
        )
    finally:
        Fname = driver.find_element_by_xpath('//*[@id="FirstName"]')
        Lname = driver.find_element_by_xpath('//*[@id="LastName"]')
    Fname.send_keys(x[3])
    Lname.send_keys(x[4])

    
    #Enters Birthdate
    Next2 = driver.find_element_by_xpath('//*[@id="iSignupAction"]')
    Next2.click()
    try:
        BD_Fields = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="BirthYear"]'))
        )
    finally:
     BirthYear = driver.find_element_by_xpath('//*[@id="BirthYear"]')
    BirthYear.send_keys("1989")

    BirthMonth = driver.find_element_by_xpath('//*[@id="BirthMonth"]')
    BirthMonth.send_keys("April")

    Birthday = driver.find_element_by_xpath('//*[@id="BirthDay"]')
    Birthday.send_keys("14")

    Next3 = driver.find_element_by_xpath('//*[@id="iSignupAction"]')
    Next3.click()

    #Finishes Sign Up
    try:
        SSIN = WebDriverWait(driver, 99999999999).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="idBtn_Back"]'))
        )
    finally: 
        NStay_Signed_In = driver.find_element_by_xpath('//*[@id="idBtn_Back"]')
        NStay_Signed_In.click()
    time.sleep(1)

    #Enters Billing Address
    driver.get('https://account.microsoft.com/billing/addresses')
    try:
        BFN = WebDriverWait(driver, 99999999999).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/main/div/div/ui-view/div[1]/div[2]/div[3]/p/a'))
    )
    finally:
        AddShipping = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/ui-view/div[1]/div[2]/div[3]/p/a')
        AddShipping.click()
    try:
        FSA = WebDriverWait(driver, 99999999999).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="address-editor-popup"]/div/div/div/form/div[1]/div[1]/input'))
    )
    finally:
        FSAddress = driver.find_element_by_xpath('//*[@id="address-editor-popup"]/div/div/div/form/div[1]/div[1]/input')
        FSAddress.click()
        FSAddress.send_keys(str (x[3]))

    LSAddress = driver.find_element_by_xpath('//*[@id="address-editor-popup"]/div/div/div/form/div[1]/div[2]/input')
    LSAddress.click()
    LSAddress.send_keys(str (x[4]))

    ADRAddress = driver.find_element_by_xpath('//*[@id="address-editor-popup"]/div/div/div/form/div[2]/div[1]/div[2]/input')
    ADRAddress.click()
    ADRAddress.send_keys(str (x[6]))

    SNDAddress = driver.find_element_by_xpath('//*[@id="address-editor-popup"]/div/div/div/form/div[2]/div[1]/div[3]/input')
    SNDAddress.click()
    SNDAddress.send_keys(str (x[7]))

    CTYAddress = driver.find_element_by_xpath('//*[@id="address-editor-popup"]/div/div/div/form/div[2]/div[1]/div[4]/input')
    CTYAddress.click()
    CTYAddress.send_keys(str (x[8]))

    PVNAddress = driver.find_element_by_xpath('//*[@id="address-editor-state-select"]')
    PVNAddress.click()
    PVNAddress.send_keys(str (x[9]))

    PTLAddress = driver.find_element_by_xpath('//*[@id="address-editor-popup"]/div/div/div/form/div[2]/div[1]/div[6]/input')
    PTLAddress.click()
    PTLAddress.send_keys(str (x[10]))

    PNBAddress = driver.find_element_by_xpath('//*[@id="address-editor-popup"]/div/div/div/form/div[3]/div[1]/div/input')
    PNBAddress.click()
    PNBAddress.send_keys(str (x[5]))
    time.sleep(1)
    Save1 = driver.find_element_by_xpath('//*[@id="ship-edit-save"]')
    Save1.click()
    time.sleep(3)

    #Enters Billing Payment
    driver.get('https://account.microsoft.com/billing/payments/')
    try:
        AP = WebDriverWait(driver, 99999999999).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/main/div/div/payment-north-star/mee-progress-view/div[4]/finished-view/div/div[1]/div[4]/div/div[2]/div/div/div/div/div'))
    )
    finally:
        time.sleep(2)
        AddPayment = driver.find_element_by_xpath('/html/body/div[1]/div[3]/main/div/div/payment-north-star/mee-progress-view/div[4]/finished-view/div/div[1]/div[4]/div/div[2]/div/div/div/div/div')
    time.sleep(0.5)       
    AddPayment.click()
    try:
        Holder1 = WebDriverWait(driver, 99999999999).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="accountHolderName"]'))
    )
    finally:
        Holder = driver.find_element_by_xpath('//*[@id="accountHolderName"]')
        Holder.click()
        Holder.send_keys(str (x[2]))
    time.sleep(1)
    cc = driver.find_element_by_xpath('//*[@id="accountToken"]')
    cc.click()
    cc.send_keys(str (x[11]))
    time.sleep(2)
    ccMonth = driver.find_element_by_xpath('//*[@id="expiryMonth"]')
    ccMonth.click()
    ccMonth.send_keys(str (x[12]))

    ccYear = driver.find_element_by_xpath('//*[@id="expiryYear"]')
    ccYear.click()
    ccYear.send_keys(str (x[13]))

    ccCVV = driver.find_element_by_xpath('//*[@id="cvvToken"]')
    ccCVV.click()
    ccCVV.send_keys(str (x[14]))
    time.sleep(1)
    try:
        Save_2 = WebDriverWait(driver, 99999999999).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pidlddc-button-saveButton"]/span'))
    )
    finally: 
        Save2 = driver.find_element_by_xpath('//*[@id="pidlddc-button-saveButton"]/span')
        Save2.click()
    try:
        close_2 = WebDriverWait(driver, 99999999999).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="id__112"]'))
    )
    finally: 
        Close2 = driver.find_element_by_xpath('//*[@id="id__112"]')
        Close2.click()
    time.sleep(2)
    
    #Send Confirmation Webhook
    f = open("C:\\Users\\Liam\\Downloads\\Microsoft Account Fill Folder\\Completed_Accounts.txt", "a+")
    f.write(x[1]+Name+":"+password+"\n")
    embed = DiscordEmbed(title="Successfully Filled Microsoft Account:farmer:", color='f44336')
    embed.add_embed_field(Name="Profile", value ="||"+x[1]+"||", inline=False)
    embed.add_embed_field(Name="User:Pass", value ="||"+x[1]+Name+":"+password+"||", inline=False)
    embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2013/02/12/09/07/microsoft-80660_960_720.png")
    embed.set_footer(text= embed.set_timestamp())
    webhook.add_embed(embed)
    response = webhook.execute(remove_embeds=True, remove_files=True)
    response = webhook.execute()
    
    #Sign out of generated profile
    ProfIcon = driver.find_element_by_xpath('//*[@id="mectrl_headerPicture"]')
    ProfIcon.click()
    time.sleep(2)
    SignOut = driver.find_element_by_xpath('//*[@id="mectrl_body_signOut"]')
    SignOut.click()
    time.sleep(2)
    driver.close()
    time.sleep(1)
    print(Name+"Generation Complete!")
    time.sleep(1)

print("All Profiles Generated!")