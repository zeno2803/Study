###########################################################
########                                         ##########
######## this is bank related simple class to    ##########
######## to work on.                             ##########
########                                         ##########
###########################################################


class Bank(object):
    """
        This class will contain function related to Banking domain
    """
    __name = ''
    __account_id = ''
    __balance = 0.0

    def __init__(self, name, account_id, initial_bal=0.0):
        """
            This is the constructor initializing name, account number and initial balance

            :param name: name of the account person
            :param account_id: account number of the person
            :param initial_bal: initial balance of the person

            :return NA

            :raises NA
        """
        self.__name = name
        self.__account_id = account_id
        self.__balance = initial_bal

    @property
    def name(self):
        """
            getter function for name args
            :return: name
        """
        return self.__name

    @property
    def account_id(self):
        """
            getter function for account_id args
            :return: account_id
        """
        return self.__account_id

    @property
    def balance(self):
        """
            getter function for balance args
            :return: balance
        """
        return self.__balance

    def withdraw(self, amount):
        """
            This function check withdraw logic from account
            :param amount: amount to be withdraw

            :returns : 0 for success
                       1 for failure
        """
        if amount > self.__balance:
            print 'Insufficient balance. Please try with less amount'
            return 1
        else:
            self.__balance -= amount
            print 'Transaction successful. Current Balance : ' + str(self.__balance)
            return 0

    def deposit(self, amount):
        """
            This function deposits the amount to balance
            :param amount: amount to be deposited

        """
        self.__balance += amount
        print 'Transaction successful. Current Balance : ' + str(self.__balance)
