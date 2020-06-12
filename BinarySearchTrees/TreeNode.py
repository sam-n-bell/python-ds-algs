
class TreeNode(object):

    def __init__(self, val: int):
        self._val = val
        self._left = None
        self._right = None

    @property
    def val(self):
        return self._val

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @left.setter
    def left(self, node):
        self._left = node

    @right.setter
    def right(self, node):
        self._right = node