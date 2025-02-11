import random
import string
from urllib.parse import urljoin


class BaseTestClass:

    main_page_url = "https://stellarburgers.nomoreparties.site/"
    register_page_url = urljoin(main_page_url, "register")
    profile_page_url = urljoin(main_page_url, "account/profile")
    login_page_url = urljoin(main_page_url, "login")

    def get_random_string_and_email(self):
        name = "".join(random.choices(string.ascii_letters, k=6))
        email = f"{name}@yandex.ru"
        return name, email

    @property
    def registered_user(self):
        email = "test666@yandex.ru"
        password = 123456
        return email, password
