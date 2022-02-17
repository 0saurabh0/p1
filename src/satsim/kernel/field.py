from .persist import Persist


class Field(Persist):

    def get_view(self):
        raise NotImplementedError

    def is_state(self):
        raise NotImplementedError

    def is_input(self):
        raise NotImplementedError

    def is_output(self):
        raise NotImplementedError

    def get_type(self):
        raise NotImplementedError
