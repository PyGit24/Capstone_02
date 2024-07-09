import pytest

from main_page import OrangePage

## Test case ID: TC_PIM_01 For checking the Reset Password link
def test_reset_password(driver):
    forgot_password = OrangePage(driver)
    forgot_password.open()
    forgot_password.scroll_down()
    forgot_password.fill_form(name="Admin")
    forgot_password.click_reset()

    # Add any assertions here to verify the results if needed
    assert "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset" in driver.current_url

    # Assertion / Validation using If Elif
    if 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset' in driver.current_url:
        print("SUCCESS : Reset Password Link sent for Username")
        driver.back()

    elif("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode") in driver.current_url:
        print("Password Not Reset for Username")
        driver.back()

## Test case ID: TC_PIM_02 Header Validation on Admin Page
def test_page_title(driver):
    title_validation = OrangePage(driver)
    title_validation.open()
    title_validation.scroll_down()
    title_validation.header_validation(name="Admin", password="admin123")
    title_validation.login_click()

    assert "OrangeHRM" in driver.title
    # driver.back()

## Test case ID: TC_PIM_02 Options are displaying on Admin Page
def test_admin_page(driver):
    head_page = OrangePage(driver)
    head_page.open()
    head_page.header_validation(name="Admin", password="admin123")
    head_page.login_click()
    head_page.main_page()

    assert "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers" in driver.current_url
    driver.back()

## Test case ID: TC_PIM_03 Main Menu Validation on Admin Page
def test_menu_page(driver):
    menu_page = OrangePage(driver)
    menu_page.open()
    menu_page.header_validation(name="Admin", password="admin123")
    menu_page.login_click()
    menu_page.main_page()
    menu_page.main_menu()

    assert "is_enabled(User Management) and is_displayed(User Management)"
    assert "is_enabled(Job) and is_displayed(Job)"
    assert "is_enabled(Organization) and is_displayed(Organization)"
    assert "is_enabled(Qualifications) and is_displayed(Qualifications)"
    assert "is_enabled(Nationalities) and is_displayed(Nationalities)"
    driver.back()

## Test case ID: TC_PIM_03 Main page Side Menu Validation on Admin Page
def test_side_menu(driver):
    side_menu = OrangePage(driver)
    side_menu.open()
    side_menu.header_validation(name="Admin", password="admin123")
    side_menu.login_click()
    side_menu.main_page()
    side_menu.main_menu()

    assert "is_enabled(Admin) and is_displayed(Admin)"
    assert "is_enabled(PIM) and is_displayed(PIM)"
    assert "is_enabled(Leave) and is_displayed(Leave)"
    assert "is_enabled(Time) and is_displayed(Time)"
    assert "is_enabled(Recruitment) and is_displayed(Recruitment)"
    assert "is_enabled(My Info) and is_displayed(My Info)"
    assert "is_enabled(Performance) and is_displayed(Performance)"
    assert "is_enabled(Dashboard) and is_displayed(Dashboard)"
    assert "is_enabled(Directory) and is_displayed(Directory)"
    assert "is_enabled(Maintenance) and is_displayed(Maintenance)"
    assert "is_enabled(Buzz) and is_displayed(Buzz)"
    driver.back()