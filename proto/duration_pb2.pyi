"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Duration(google.protobuf.message.Message):
    """*
    A length of time in seconds.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SECONDS_FIELD_NUMBER: builtins.int
    seconds: builtins.int
    """*
    The number of seconds
    """
    def __init__(
        self,
        *,
        seconds: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["seconds", b"seconds"]) -> None: ...

global___Duration = Duration