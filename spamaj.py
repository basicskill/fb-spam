#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, os
import config
from pyvirtualdisplay import Display



dir_path = os.path.dirname(os.path.realpath(__file__))
drajver = dir_path + '/chromedriver'

def poruka(br, br_puta, PORUKA):
	box = br.find_element('xpath', "//div[contains(@class,'_5rpu') and @role='combobox']")
	try:
		for ink in range(0, br_puta):
			box.send_keys(PORUKA)
			box.send_keys(Keys.ENTER)
	except:
		poruka(br, br_puta, PORUKA)
	br.quit()


def logovanje(IME, PORUKA):
	br = webdriver.Chrome(executable_path=drajver)
	br.get('https://www.messenger.com/t/' + IME)

	user = br.find_element_by_css_selector('#email')
	password = br.find_element_by_css_selector('#pass')
	login =  br.find_element_by_css_selector('#loginbutton')

	user.send_keys(config.MEJL)
	password.send_keys(config.PASS)
	login.click()
	poruka(br, 23, PORUKA)

if __name__ == '__main__':
	ekran = Display(visible=0, size=(800, 600))
	ekran.start()
	
	Ime = sys.argv[1]	
	Poruka = sys.argv[2]
	br_puta = sys.argv[3]
	logovanje(Ime, Poruka)
	ekran.stop()
