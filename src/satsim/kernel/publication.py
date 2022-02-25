import enum


class ViewKind(enum.IntEnum):
    Hidden = 0
    Debug = 1
    Expert = 2
    All = 3


class Publication:

    def publish_field(
            self,
            name,
            description,
            reference,
            view=ViewKind.All,
            state=True,
            input=False,
            output=False):
        # TODO: implement
        pass
