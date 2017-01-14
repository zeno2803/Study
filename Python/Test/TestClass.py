#########################################################################################
#### This script contains module related detail.                                     ####
#########################################################################################


class TestClass(object):
    """
        This class contains the method related to mdules
    """

    def __init__(self):
        """
            This is the constructor of the module
        """
        print 'message is set in constructor'
        self.__message = ''

    def display(self):
        """
            This method the message
        """
        if self.__message:
            print 'printing the message inputted : '
            print self.__message
        else:
            print 'No message inputted'

    @property
    def message(self):
        """
            this is getter method, returns the message
        :return: __message
        """
        print 'I am in getter method'
        return self.__message

    @message.setter
    def message(self, msg):
        """
            This is setter message
        :param msg: message value to be set
        """

        print 'I am in setter method'
        self.__message = msg
