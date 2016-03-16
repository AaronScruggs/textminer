import re


def words(text):
    answer = re.findall(r"[\w-]*[a-z]+", text)
    if answer is None or len(answer) == 0:
        return None
    return answer


def phone_number(text):
    get_all = re.findall(r"[0-9]*", text)
    numbers = "".join([x for x in get_all if x != ""])
    if len(numbers) != 10:
        return None

    first = numbers[:3]
    second = numbers[3:]
    answer = {"area_code": first,
              "number": "{}-{}".format(second[:3], second[3:])
              }
    return answer


def money(text):
    checked = re.search(r"^\W\d+(?:,\d{3})*(?:\.\d{2})?", text)

    if checked is None or checked.group() != text:
        return None

    currency = re.search(r"^\W", text)
    amount = re.findall(r"(?:\d{1,3})+(?:\.\d{2})?", text)

    return {"currency": currency.group(), "amount": float("".join(amount))}


def zipcode(text):
    z = re.search(r"^\d{5}(?:\-\d{4})?$", text)
    if z is None:
        return None
    z = z.group()[:5]
    plus = re.search(r"\-\d{4}$", text)
    if plus is not None:
        plus = plus.group()[-4:]
    return {"zip": z, "plus4": plus}


def date(text):
    """
    This function assumes that dates will be ordered either year/month/day
    or month/day/year as they are in the test cases. A date entered as
    day/month/year would not be handled correctly by this function.
    """
    entries = re.findall(r"\d*", text)
    dates = [x for x in entries if x != ""]
    if len(dates) != 3:
        return None

    if len(dates[0]) == 4:
        year = dates[0]
        month = dates[1]
        day = dates[2]
    else:
        year = dates[2]
        month = dates[0]
        day = dates[1]

    return {"year": int(year), "month": int(month), "day": int(day)}
