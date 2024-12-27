from selene import browser, have, by
import os

first_name = 'James'
last_name = 'Smith'
email = 'jamessmith007@testmail.test'
gender = 'Male'
mobile = '0101234567'
birth_day = '27'
birth_month = 'August'
birth_year = '1996'
subjects = 'Maths'
hobbies = 'Music'
picture = f'../resources/test.jpeg'
current_address = '53 New Oxford Street, London, WC1A 1BL'
state = 'Haryana'
city = 'Karnal'


def test_fill_form(browser_management):
    browser.open('/automation-practice-form')

    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(email)
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type(mobile)
    # select date of birth
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="7"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1996"]').click()
    browser.element('.react-datepicker__day--027').click()

    browser.element('#subjectsInput').type(subjects).press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath(picture))
    browser.element('#currentAddress').type(current_address)
    browser.element('#state').click().element(by.text(state)).click()
    browser.element('#city').click().element(by.text(city)).click()

    browser.element("#submit").click()

    assert browser.element('.table-responsive').should(have.text('Student Name')).should(
        have.text(f'{first_name} {last_name}'))
    assert browser.element('.table-responsive').should(have.text('Student Email')).should(have.text(email))
    assert browser.element('.table-responsive').should(have.text('Gender')).should(have.text(gender))
    assert browser.element('.table-responsive').should(have.text('Mobile')).should(have.text(mobile))
    assert browser.element('.table-responsive').should(have.text('Date of Birth')).should(
        have.text(f'{birth_day} {birth_month},{birth_year}'))
    assert browser.element('.table-responsive').should(have.text('Subjects')).should(have.text(subjects))
    assert browser.element('.table-responsive').should(have.text('Hobbies')).should(have.text(hobbies))
    assert browser.element('.table-responsive').should(have.text('Picture')).should(
        have.text(os.path.basename(picture)))
    assert browser.element('.table-responsive').should(have.text('Address')).should(have.text(current_address))
    assert browser.element('.table-responsive').should(have.text('State and City')).should(have.text(f'{state} {city}'))
