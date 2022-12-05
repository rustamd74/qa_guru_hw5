from selene.support.shared import browser
from selene import have, be
import os


def test_filling_form(open_browser):
    browser.element('#firstName').should(be.blank).type('John')
    browser.element('#lastName').should(be.blank).type('Doe')
    browser.element('#userEmail').should(be.blank).type('johndoe@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('2223331110')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select>[value="4"').click()
    browser.element('.react-datepicker__year-select>[value="1901"]').click()
    browser.element('.react-datepicker__day--004').click()
    browser.element('#subjectsInput').should(be.blank).type('QA Automation')
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').set_value(os.path.abspath('file/python_label.png'))
    browser.element('#currentAddress').should(be.blank).type('221b, Baker street')
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Lucknow').press_enter()
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text(
        'John Doe'and 'johndoe@gmail.com'and 'Male'and '2223331110'and '04 April,1901'and ''and 'Sports,Music'and
        'python_label.png'and '221b, Baker street'and 'Uttar Pradesh Lucknow'))
