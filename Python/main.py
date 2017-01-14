#!/usr/bin/python
#import Test.TestClass

from Test.TestClass import *
from Function import convert_to_title


def main():
    """
        This is the main of the code
    """
    print 'Hello World\n'

    name = raw_input("UserName : ")
    password = raw_input("Password : ")

    print name, password

    test_object = TestClass()
    test_object.display()
    test_object.message = "I am a very lazy lazy boy"
    print test_object.message

    print convert_to_title(2), convert_to_title(1), convert_to_title(25), convert_to_title(26), convert_to_title(27), convert_to_title(52)

    return


if __name__ == '__main__':
    main()
