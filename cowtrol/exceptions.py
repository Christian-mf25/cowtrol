from rest_framework.exceptions import APIException


class CustomException(APIException):
    default_detail = "You can't perform this action."

    def __init__(self, detail=None, code=None):
        self.status_code = code
        super().__init__(detail, code)