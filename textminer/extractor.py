import re


def phone_numbers(text):
    matches = re.findall(r"\(\d{3}\) \d{3}\-\d{4}", text)
    return matches
