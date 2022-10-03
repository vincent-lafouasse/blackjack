#####################################################################
# For more complete methods, refer to UserList() in the CPython source...
# https://github.com/python/cpython/blob/208a7e957b812ad3b3733791845447677a704f3e/Lib/collections/__init__.py#L1215
#####################################################################

try:
    # Python 3
    from collections.abc import MutableSequence
except ImportError:
    # Python 2.7
    from collections import MutableSequence

class MyList(MutableSequence):
    """A container for manipulating lists of hosts"""
    def __init__(self, data=None):
        """Initialize the class"""
        super(MyList, self).__init__()
        if (data is not None):
            self._list = list(data)
        else:
            self._list = list()

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self._list)

    def __len__(self):
        """List length"""
        return len(self._list)

    def __getitem__(self, ii):
        """Get a list item"""
        if isinstance(ii, slice):
            return self.__class__(self._list[ii])
        else:
            return self._list[ii]

    def __delitem__(self, ii):
        """Delete an item"""
        del self._list[ii]

    def __setitem__(self, ii, val):
        # optional: self._acl_check(val)
        self._list[ii] = val

    def __str__(self):
        return str(self._list)

    def insert(self, ii, val):
        # optional: self._acl_check(val)
        self._list.insert(ii, val)

    def append(self, val):
        self.insert(len(self._list), val)

if __name__=='__main__':
    foo = MyList([1,2,3,4,5])
    foo.append(6)
    print(foo)  # <MyList [1, 2, 3, 4, 5, 6]>

    for idx, ii in enumerate(foo):
        print("MyList[%s] = %s" % (idx, ii))
