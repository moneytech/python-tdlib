from ..factory import Type


class video(Type):
	duration = None  # type: "int32"
	width = None  # type: "int32"
	height = None  # type: "int32"
	file_name = None  # type: "string"
	mime_type = None  # type: "string"
	has_stickers = None  # type: "Bool"
	supports_streaming = None  # type: "Bool"
	thumbnail = None  # type: "photoSize"
	video = None  # type: "file"
