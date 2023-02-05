from rest_framework.response import Response

class FormattedResponse:
    def __init__(self, error=False, msg=None, data={}) -> None:
        self.is_error = error
        self.status_msg = 'Data fetched succcesfully.'
        self.status_code = 0    # No error
        if error:
            self.status_msg = 'Error Occured.'
            self.status_code = -1
        if msg:
            self.status_msg = msg
            
        self.response_dict = {
                'custom_status_code': self.status_code,
                'status_msg' : self.status_msg,
                'data_dict' : data
            }
    def create(self):
        return Response(self.response_dict)
    def __str__(self) -> str:
        return self.create()