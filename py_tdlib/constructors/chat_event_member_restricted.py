from ..factory import Type


class chatEventMemberRestricted(Type):
	user_id = None  # type: "int32"
	old_status = None  # type: "ChatMemberStatus"
	new_status = None  # type: "ChatMemberStatus"
