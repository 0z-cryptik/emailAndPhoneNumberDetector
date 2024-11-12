import pyperclip, re
from regexPatterns import email_pattern, phone_no_pattern, american_no_pattern

email_regex = re.compile(email_pattern, re.VERBOSE)
phone_no_regex = re.compile(phone_no_pattern)
american_no_regex = re.compile(american_no_pattern, re.VERBOSE)

text = str(pyperclip.paste())

def process_us_number(groups: list) -> str:
    phoneNum = "-".join([groups[1], groups[3], groups[5]])

    if groups[8] != "":
        phoneNum += " x" + groups[8]

    return phoneNum

matches = []

for group in email_regex.findall(text):
    matches.append(group)

for group in phone_no_regex.findall(text):
    matches.append(group)

# returns matches in tuples because the pattern uses '()'
for groups in american_no_regex.findall(text):
    phone_num = process_us_number(groups)
    matches.append(phone_num)

if len(matches) == 0:
    print("no matches were found")
else:
    print("\n".join(matches))
