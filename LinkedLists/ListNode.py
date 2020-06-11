

class ListNode(object):

    def __init__(self, val: int):
        self._val = val
        self._next = None

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, number: int):
        self._val = number

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, val):
        self._next = val

    def __repr__(self):
        response = f'Val {self._val} pointing to '
        if not self._next:
            response += 'None'
        else:
            response += f'{self._next.val}'
        return response
