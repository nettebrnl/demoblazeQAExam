import playwright as playwright
from playwright.sync_api import sync_playwright, Page, expect
import libraries.data.common as dCommon

def goToURL(page: Page, url):
    page.goto(url)
    page.wait_for_load_state('load')
    
def clickElem(page: Page, elem):
    page.locator(elem).click(force=True)
    
def waitElemToBeVisible(page: Page, elem, intTimeOut = dCommon.time.intDefTimeOut):
    page.wait_for_selector(elem, state='visible', timeout = intTimeOut)
    
def waitAndClickElemText(page: Page, strText, strParent = '', intIndex = 1, intWaitTime = 1):
    page.locator(f'({strParent}//*[contains(text(),"{strText}")])[{intIndex}]').click(force=True)
    
def setElem(page: Page, elem, strValue):
    page.locator(elem).fill(strValue)
    
def waitAndClickElem(page: Page, elem):
    waitElemToBeVisible(page, elem)
    clickElem(page, elem)
    
def waitForLoadState(page: Page, strState = 'load'):
    page.wait_for_load_state(strState)