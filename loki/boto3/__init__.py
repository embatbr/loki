"""
Similar to the real boto3 `__init__.py` file.

For more info, see https://github.com/boto/boto3/blob/develop/boto3/__init__.py
"""


from loki.boto3.session import Session


DEFAULT_SESSION = None

MOCK_PATHS = {
    's3_bucket_path' : None
}


def setup_default_session():
    global DEFAULT_SESSION
    DEFAULT_SESSION = Session(**MOCK_PATHS)


def _get_default_session():
    if DEFAULT_SESSION is None:
        setup_default_session()

    return DEFAULT_SESSION


def client(*args, **kwargs):
    return _get_default_session().client(*args)


def resource(*args, **kwargs):
    return _get_default_session().resource(*args)


def mock(**kwargs):
    for (key, value) in kwargs.items():
        MOCK_PATHS[key] = value
