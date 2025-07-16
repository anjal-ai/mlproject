# exception.py
import sys
import logging


class CustomException(Exception):
    """
    Custom exception class to log and raise errors with more context.
    """

    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, error_detail)

    def get_detailed_error_message(self, error_message: str, error_detail: sys):
        """
        Creates a detailed error message with file name and line number.
        """
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error occurred in script: [{file_name}] at line [{line_number}] - {error_message}"

    def __str__(self):
        return self.error_message
