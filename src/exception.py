import logging
import sys

# def error_msg_detail(error, error_detail: sys):
#     _, _, exc_tb = error_detail.exc_info()
#     file_name = exc_tb.tb_frame.f_code.co_filename
#     error_message = f"Error occured in file: {file_name}, line: {exc_tb.tb_lineno}, error: {str(error)}"

#     return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message = self.error_msg_detail(error=error_message, error_detail=error_detail)

    
    def error_msg_detail(self, error, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message = f"\nOccured in file: {file_name}\nline: {exc_tb.tb_lineno}\nerror: {str(error)}"

        return error_message
    

    def __str__(self) -> str:
        return self.error_message
    

# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by zero exception")
#         raise CustomException(error_message=e, error_detail=sys)