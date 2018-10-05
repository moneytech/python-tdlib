from ..factory import Method, Type


class secretChat(Type):
    # Represents a secret chat

    id = None  # type: "int32"
    user_id = None  # type: "int32"
    state = None  # type: "SecretChatState"
    is_outbound = None  # type: "Bool"
    ttl = None  # type: "int32"
    key_hash = None  # type: "bytes"
    layer = None  # type: "int32"


class getSecretChat(Method):
    # Returns information about a secret chat by its identifier. This
    # is an offline request, @secret_chat_id Secret chat identifier

    secret_chat_id = None  # type: "int32"
