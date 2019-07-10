from web_helpers import *
from selenium import webdriver
import speech_recognition as sr
import tkinter as tk

Commands=['messages','notifications','request','online']


def process(comm,MessageBox):
    command=comm.split()
    if command[0] not in Commands:
        MessageBox.insert(tk.END, "Command Error :(.. Try Again!! \n")
        return
    if(command[0]=='messages'):
        wait_till_pageloads(browser, By.ID, 'mercurymessagesCountValue')
        count=browser.find_element_by_id('mercurymessagesCountValue').get_attribute("innerText")
        MessageBox.insert(tk.END,"You Have "+str(count)+" New Messages!!\n")
    elif(command[0]=='notifications'):
        wait_till_pageloads(browser, By.ID, 'notificationsCountValue')
        count = browser.find_element_by_id('notificationsCountValue').get_attribute("innerText")
        MessageBox.insert(tk.END, "You Have " + str(count) + " New Notifications!!\n")
    elif(command[0]=='request'):
        wait_till_pageloads(browser, By.ID, 'requestsCountValue')
        count = browser.find_element_by_id('requestsCountValue').get_attribute("innerText")
        MessageBox.insert(tk.END, "You Have " + str(count) + " New Requests!!\n")
    else:
        pass

def login_facebook(username,password):
    try:
        global browser
        browser = webdriver.Chrome(chrome_options=set_options(), executable_path='E:\chromedriver.exe')
        browser.get('https://www.facebook.com/')
        browser.minimize_window()

        wait_till_pageloads(browser,By.ID,'email')
        userelem = browser.find_element_by_id('email')
        userelem.send_keys(username)
        passwordd = browser.find_element_by_id('pass')
        passwordd.send_keys(password)
        log = browser.find_element_by_id('loginbutton')
        log.click()


    except Exception as errormessage:
        print(errormessage)


def voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say Command")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            # print("you said: " + text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not request results from Google")

