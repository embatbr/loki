"""
This module is a mock of the real `boto3.session.py`. The class `Session` contains
methods
"""


from boto3.exceptions import ResourceNotExistsError


class Session(object):

    def __init__(self, s3_bucket_path=None):
        __s3_bucket_path = s3_bucket_path if s3_bucket_path else '~'

        # TODO change value of 's3' by an object of type S3Resource or similar
        self.services = {
            's3' : {
                'root_path' : __s3_bucket_path
            }
        }

    def client(self, service_name):
        pass

    def resource(self, service_name):
        if not service_name in self.services:
            available = self.services.keys()
            raise ResourceNotExistsError(service_name, available, False)

        # TODO change by an object of type Resource or similar
        return self.services[service_name]
