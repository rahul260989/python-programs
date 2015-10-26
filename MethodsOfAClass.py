# Small program to know all the methods of a class

import inspect


class Test(object):
    """ My family
    """

    def meth1(self, *args):
        return 1

    @staticmethod
    def meth2():
        return [1, 3]

    @classmethod
    def meth3(cls):
        return "aaa"


print inspect.getmembers(Test, predicate=inspect.ismethod)