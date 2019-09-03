# Generated by Selenium IDE
import pytest
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestSearch():
  def setup_method(self, method):
    self.vars = {}
    desired_cap = {
    'platform': "Mac OS X 10.13",
    'browserName': "safari",
    'version': "11.1",
    'build': "Onboarding Sample App - Python",
    'name': "2-user-site",
    }
    username = os.environ["SAUCE_USERNAME"]
    access_key = os.environ["SAUCE_ACCESS_KEY"]
    self.driver = webdriver.Remote(command_executor='https://{}:{}@ondemand.eu-central-1.saucelabs.com/wd/hub'.format(username, access_key), desired_capabilities=desired_cap)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_search(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(814, 860)
    self.driver.find_element(By.ID, "exampleInputAddress").click()
    self.driver.find_element(By.ID, "ui-id-11").click()
    self.driver.find_element(By.ID, "exampleInputAddress").send_keys("2 Rue des Clos Moreaux 92190 Meudon")
    self.driver.find_element(By.ID, "exampleInputHour").click()
    self.driver.find_element(By.ID, "exampleInputHour").send_keys("1")
    self.driver.find_element(By.ID, "exampleInputMin").click()
    self.driver.find_element(By.ID, "exampleInputMin").send_keys("1")
    self.driver.find_element(By.ID, "btn-1").click()
  

