from automation import __version__
from automation.automation import *
import re



def test_version():
    assert __version__ == '0.1.0'


def test_import():
    assert phone_regex, email_regex

def test_phone_numbers():
    text = '281-222-2222'
    actual = re.match(phone_regex, text).group()
    expected = text
    assert actual == expected

def test_email():
    text = 'david@email.com'
    actual = re.match(email_regex, text).group()
    expected = text
    assert actual == expected
