import libraries.page.profile as pProfile
import libraries.util.common as uCommon
import libraries.data.common as dCommon

class com:
    """COMMON"""    
    def goToDemoblazeURL(page):
        """ 
        Objective: Go to Demoblaze URL
        
        param: None
        returns: None
        Author: abernal_20240823
        """
        uCommon.goToURL(page, f'{dCommon.url.strBaseUrl}')
        uCommon.waitElemToBeVisible(page, pProfile.com.productStoreLbl)

class li:
    """LOGIN"""
    def login(page, strUsername, strPassword):
        """ 
        Objective: Click Login And Fill Details
        
        param strUserName: User Name
        param strPassword: Password
        returns: None
        Author: abernal_20240823
        """
        uCommon.waitAndClickElem(page, pProfile.com.loginBtn)
        uCommon.waitElemToBeVisible(page, pProfile.li.loginBtn)
        uCommon.setElem(page, pProfile.li.usernameLbl, strUsername)
        uCommon.setElem(page, pProfile.li.passwordLbl, strPassword)
        uCommon.waitAndClickElem(page, pProfile.li.loginBtn)
        uCommon.waitForLoadState(page)
        uCommon.waitElemToBeVisible(page, pProfile.com.logoutBtn)
        
class lo:
    """LOGOUT"""
    def logout(page):
        """ 
        Objective: Click logout
        
        param: None
        returns: None
        Author: abernal_20240823
        """
        uCommon.waitAndClickElem(page, pProfile.com.logoutBtn)
        uCommon.waitElemToBeVisible(page, pProfile.com.loginBtn)