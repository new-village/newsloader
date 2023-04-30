""" load.py
"""

def load():
    """ load
    """
    loader = WsjLoader()
    return loader.exec()


class NsLoader():
    """ base class of Loaders """
    def __init__(self):
        self.title = None
        self.body = None


class WsjLoader(NsLoader):
    """ Entry data Loader """
    def exec(self):
        """ Description
        """
        self.title = "title"
        self.body = "body"
        return self
