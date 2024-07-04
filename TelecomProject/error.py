import os
import sys
import time
from animation.colors import *
from TelecomProject.telecom_db import option, already_user


def log_error(error: Exception):
    """
    Logs errors to a file.

    Parameters
    ----------
    error : Exception
        The exception object containing details of the error to be logged.

    Notes
    -----
    This function captures the exception details including the type of exception,
    the file name where the exception occurred, the line number, and a string
    representation of the error. It logs this information to a file named 'notification/error.txt'
    and also prints the error to the console with a delay of 3 seconds.
    """
    # Get the exception information
    exc_type, exc_obj, exc_tb = sys.exc_info()

    # Open the error log file in write mode
    with open('../notification/error.txt', 'w') as file:
        # Write the exception details to the file
        file.write(
            f'{exc_type}, \n'  # Write the type of exception
            f'{os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]}\n'  # Get the filename where the exception occurred
            f'{exc_tb.tb_lineno}, \n'  # Write the line number where the exception occurred
            f'Error: {repr(error)}'  # Write the string representation of the error
        )

    # Print the error message to the console
    print(red, f'\nError -> {repr(error)}', end, sep='')

    # Delay for 3 seconds to allow the user to read the error message
    time.sleep(3)


def go_back(return_place, ):
    """Placeholder function to handle going back to a previous step.
        This should be defined elsewhere in the actual implementation.

    Args:
        return_place (str): The place to return to ('script' or 'signed_in').
        auth (Authentication, optional): The authentication object. Defaults to None.
    """
    if return_place == 'script':
        option()
    if return_place == 'signed_in':
        already_user()

exc_type, exc_obj, exc_tb = sys.exc_info()

# Open the error log file in write mode
# with open('notification/error.txt', 'w',  encoding='utf-8') as file:
#     # Write the exception details to the file
#     file.write(
#         f'{exc_type}, \n'  # Write the type of exception
#         f'{os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]}\n'  # Get the filename where the exception occurred
#         f'{exc_tb.tb_lineno}, \n'  # Write the line number where the exception occurred
#         f'Error: {repr(error)}'  # Write the string representation of the error
#     )
#
# # Print the error message to the console
# print(red, f'\nError -> {repr(error)}', end, sep='')
#
# # Delay for 3 seconds to allow the user to read the error message
# time.sleep(3)

channel = 'test'

with open(f'../notification/{channel}.txt', 'a', encoding='utf-8') as file:
    file.write(message)
    file.write('\n')

