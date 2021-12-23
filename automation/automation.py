import re

with open('./automation/potential-contacts.txt') as file:
    text_content = file.read()

phone_regex = r'\d\d\d-\d\d\d-\d\d\d\d'

email_regex = r'\w*@\w*.\w*'

potential_phone_numbers = re.findall(phone_regex, text_content)

potential_emails = re.findall(email_regex, text_content)

with open('./automation/phone_numbers.txt', 'w') as file:
    for number in potential_phone_numbers:
        file.write(number)
        file.write('\n')

with open('./automation/emails.txt', 'w') as file:
    for email in potential_emails:
        file.write(email)
        file.write('\n')