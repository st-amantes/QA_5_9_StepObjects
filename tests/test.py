from datetime import date

from pages.registration_pages import RegistrationPage
from pages.user import User


def test_authorization():
    # исходные данные
    student = User(
        first_name='Albert',
        last_name='Ivanov',
        email='ALLIIVAN@mail.ru',
        gender='Male',
        mobile='8954567689',
        date_of_birth=date(1993, month=4, day=28),
        month='April',
        subjects='Physics',
        hobbies1='Sports',
        hobbies2='Reading',
        hobbies3='Music',
        picture='pictures.jpg',
        addrees='Pharabi street 18',
        state='Rajasthan',
        city='Jaipur',
    )
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.register(student)

    # THEN
    registration_page.assert_register_user_info(student)
