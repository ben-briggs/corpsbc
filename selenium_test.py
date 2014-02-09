#!/usr/bin/env python
__author__ = 'ben'

import timeit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import time

print 'Initializing display...'
display = Display(visible=0, size=(800, 600))
display.start()

print 'Starting Firefox...'
browser = webdriver.Firefox()


def test():
    print 'Initializing test...'
    browser.get('http://www.google.com')
    time.sleep(1)
    q = browser.find_element_by_name('q')
    q.send_keys("Jack's Family Restaurants")
    q.send_keys(Keys.ENTER)

    time.sleep(1)

    print 'Displaying result...'
    results = browser.find_elements_by_class_name('g')
    for result in results:
        #try:
            print '-' * 80
            print result.text
        #except ex:
            #            pass
    return 0

#test()
print timeit.timeit("test()", setup="from __main__ import test", number=10)
browser.close()
display.stop()
