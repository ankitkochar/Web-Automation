from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from sys import argv
from time import sleep

name = "Sukhi.018"
file_path = "book_scrape.csv"

browser = webdriver.Chrome("C:\\Users\\Ankit\\Documents\\Codes\\Python Codes\\Web Automation\\chromedriver.exe")
browser.get( "https://www.instagram.com/" )	
browser.maximize_window()
# exit()
def wait( css_selector ):
	
	try:
		WebDriverWait( browser , 20 ).until( EC.visibility_of_element_located( ( By.CSS_SELECTOR , css_selector ) ) )
	except TimeoutException:
		exit()

def Login( username , password ):

	wait( "input[name='username']" )
	browser.find_element_by_name( "username" ).send_keys( username )
	browser.find_element_by_name( "password" ).send_keys( password )
	browser.find_element_by_css_selector( "button.L3NKy[type='submit']" ).click()

with open( "id_pass.txt" ) as file:

	username = file.readline().strip( "\n" )
	password = file.readline().strip( "\n" )

Login( username , password )
# exit()
wait( "section.ABCxa" )
browser.get( "https://www.instagram.com/{}".format( name ) )
# exit()

wait('button.L3NKy[type="button"]')
browser.find_element_by_css_selector( '.sqdOP.L3NKy._4pI4F._8A5w5' ).click()
wait( 'body > div.RnEpo.Yx5HN > div > div > div' )
browser.find_element_by_css_selector( 'button.aOOlW.HoLwm' ).click()
wait('#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.ItkAi > textarea')
message_box=browser.find_element_by_css_selector( '#react-root > section > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.DPiy6.Igw0E.IwRSH.eGOV_.vwCYk > div.uueGX > div > div.Igw0E.IwRSH.eGOV_._4EzTm > div > div > div.Igw0E.IwRSH.eGOV_.vwCYk.ItkAi > textarea' )


with open( file_path , "r" ) as file:

	line=file.readline()

	while line!="":

		message_box.send_keys( line.strip("\n") )
		# sleep(7)
		message_box.send_keys( Keys.ENTER )
		line=file.readline()
		# exit()

