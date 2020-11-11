def factorial(number):
    """
    Calculate the factorial for a number
    :param number: to calculate the factorial
    :return: factorial of n
    """
    return 1 if number == 1 else number * factorial(number - 1)
