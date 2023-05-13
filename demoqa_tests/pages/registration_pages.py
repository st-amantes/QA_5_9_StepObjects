import dataclasses
import os
from selene import browser, have, command


@dataclasses.dataclass
class RegistrationPage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.fullscreen_window()

    def __init__(self):
        self.state = browser.all('[id^=react-select][id*=option]')
        self.adress = browser.element('#currentAddress')
        self.element = browser.element

    def register(self, student):
        self.element('#firstName').send_keys(student.first_name)
        self.element('#lastName').send_keys(student.last_name)
        self.element('#userEmail').send_keys(student.email)
        self.element(f'[name = gender][value = {student.gender}]+label').click()
        self.element('#userNumber').send_keys(student.mobile)
        self.element('#dateOfBirthInput').click()

        self.element('.react-datepicker__month-select').send_keys(student.date_of_birth.month)
        self.element('.react-datepicker__year-select').send_keys(student.date_of_birth.year)
        self.element(f'.react-datepicker__day--0{student.date_of_birth.day}').click()

        self.element('#subjectsInput').send_keys(student.subjects).press_enter()

        browser.all('[for = hobbies-checkbox-1]').element_by(have.exact_text(student.hobbies1)).click()
        browser.all('[for = hobbies-checkbox-2]').element_by(have.exact_text(student.hobbies2)).click()
        browser.all('[for = hobbies-checkbox-3]').element_by(have.exact_text(student.hobbies3)).click()

        os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../tests/resources/pictures.jpg'))
        browser.driver.execute_script(
            'document.querySelector("#fixedban").remove()')

        self.element('#currentAddress').perform(command.js.scroll_into_view)
        self.element('#currentAddress').send_keys(student.addrees)
        browser.element('#state').click()

        self.state.element_by(have.exact_text(student.state)).click()
        browser.element('#city').click()

        self.state.element_by(have.exact_text(student.city)).click()
        browser.element('#city').click()

        self.element('#submit').perform(command.js.click)

    def assert_register_user_info(self, student):
        full_name = f'{student.first_name} {student.last_name}',
        email = student.email,
        gender = student.gender,
        number = student.mobile,
        day_brith = f'{student.date_of_birth.day} {student.month},{student.date_of_birth.year}',
        subject = student.subjects,
        hobbies = f'{student.hobbies1}, {student.hobbies2}, {student.hobbies3}',
        picture = student.picture,
        adress = student.addrees,
        city = f'{student.state} {student.city}'

        browser.all('.table-responsive td:nth-child(2)').should(
            have.exact_texts(
                full_name,
                email,
                gender,
                number,
                day_brith,
                subject,
                hobbies,
                '',
                adress,
                city,
            ))
