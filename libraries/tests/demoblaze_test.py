import pytest

import libraries.data.profile as dProfile
import libraries.util.profile as uProfile

@pytest.mark.blazeTest()
def test_TC001_User_should_be_able_to_login_and_logout(page):
    """Step 1: Navigate to Demoblaze Website"""
    uProfile.com.goToDemoblazeURL(page)
    
    """Step 2: Proceed to Login"""
    uProfile.li.login(page, dProfile.login.strUsername, dProfile.login.strPassword)
    
    """Step 3: Proceed to Logout"""
    uProfile.lo.logout(page)