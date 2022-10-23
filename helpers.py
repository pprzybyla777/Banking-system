class Helpers:

    @staticmethod
    def is_amount_valid(amount):
        if Helpers.is_correct_type(amount):
            if Helpers.is_nonnegative(amount):
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def is_correct_type(amount) -> bool:
        "Checks if amount is an INT or Float with max two decimal points"
        if type(amount) == int:
            return True
        elif type(amount) == float:
            integral, fractional = str(amount).split('.')
            if len(fractional) == 1 or len(fractional) == 2:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def is_nonnegative(amount) -> bool:
        if amount > 0:
            return True
        else:
            return False


    @staticmethod
    def are_funds_sufficient(account_balance, amount):
        """funds must be equal or greater than amount"""
        if account_balance >= amount:
            return True
        else:
            return False
