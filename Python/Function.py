import string


def convert_to_title(num):
    title = ''
    alist = string.uppercase
    while num:
        mod = (num-1) % 26
        num = int((num - mod) / 26)
        title += alist[mod]
    return title[::-1]
