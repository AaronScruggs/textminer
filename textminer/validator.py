import re


def results(match, text):
    """ Helper function for returning the results. """
    if match is None or text == "":
        return False
    else:
        return match.group() == text


def binary(text):
    match = re.search(r"[01]*", text)
    return match.group()


def binary_even(text):
    match = re.search(r"[01]*0$", text)
    return results(match, text)


def hex(text):
    match = re.search(r"[0-9A-F]+", text)
    return results(match, text)


def word(text):
    match = re.search(r"[\w-]*[a-z]+", text)
    return results(match, text)


def words(text, count=False):
    if len(text) < 1:
        return False

    for w in text.split():
        searched = re.search(r"[\w-]*[a-z]+", w)
        if searched is None or searched.group() != w:
            return False

    if not count:
        return True
    elif count == len(text.split()):
        return True,
    else:
        return False


def phone_number(text):

    match = re.search(r"\(?\d{3}[\)-\.]? ?\d{3}[-\.]?\d{4}", text)
    print(match)
    return results(match, text)


def money(text):

    match = re.search(r"^\$\d+(?:,\d{3})*(?:\.\d{2})?", text)
    return results(match, text)


def zipcode(text):
    match = re.search(r"^\d{5}(?:-\d{4})?", text)
    return results(match, text)


def date(text):
    """
    Used two different searches to account for different formats,
    where the four digit year can be either the first or last entry.
    """
    match = re.search(r"\d{1,2}[\-/]{1}\d{1,2}[\-/]{1}\d{4}", text)
    if match is None:
        match = re.search(r"\d{4}[\-/]{1}\d{1,2}[\-/]{1}\d{1,2}", text)
    return results(match, text)
