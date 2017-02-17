#!/usr/bin/python
# import Test.TestClass

from Test.TestClass import *
from Function import convert_to_title
from Manu.Bank import *
import logging
import datetime

timestamp = str(datetime.datetime.now()).replace(' ', '_').replace('-', '_').replace(':', '_').split('.')[0]
formatter = '%(asctime)s :: %(filename)s :: %(funcName)s :: %(lineno)d ===> %(message)s'
log_file_name = 'logfile_' + timestamp + '.txt'
logging.basicConfig(filename=log_file_name, level=logging.DEBUG, format=formatter)
print log_file_name


def main():
    """
        This is the main of the code
    """
    print 'Hello World\n'
    logging.info('helllllooooooooooo')
    logging.warning('gtyuojgjkl')

    name = raw_input("UserName : ")
    password = raw_input("Password : ")
    logging.debug('this is my first logger')

    print name, password

    # test_object = TestClass()
    # test_object.display()
    # test_object.message = "I am a very lazy lazy boy"
    # print test_object.message

    test_obj = Bank('Abhishek', '1234567890')
    print 'Bank Details : \n'
    test_obj.deposit(100)
    print '\n', test_obj.name, test_obj.account_id, test_obj.balance

    print convert_to_title(2), convert_to_title(1), convert_to_title(25), convert_to_title(26), convert_to_title(27), \
        convert_to_title(52)

    return 0


if __name__ == '__main__':
    main()
