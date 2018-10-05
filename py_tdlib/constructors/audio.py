from ..factory import Type


class audio(Type):
    # Describes an audio file. Audio is usually in MP3 format
    # @duration Duration of the audio, in seconds; as defined by
    # the sender, @title Title of the audio; as defined by
    # the sender, @performer Performer of the audio; as defined by the sender

    duration = None  # type: "int32"
    title = None  # type: "string"
    performer = None  # type: "string"
    file_name = None  # type: "string"
    mime_type = None  # type: "string"
    album_cover_thumbnail = None  # type: "photoSize"
    audio = None  # type: "file"
