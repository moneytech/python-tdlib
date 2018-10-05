from ..factory import Type


class document(Type):
    # Describes a document of any type, @file_name Original name of
    # the file; as defined by the sender, @mime_type MIME type
    # of the file; as defined by the sender

    file_name = None  # type: "string"
    mime_type = None  # type: "string"
    thumbnail = None  # type: "photoSize"
    document = None  # type: "file"
