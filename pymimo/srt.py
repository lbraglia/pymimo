import re

class srt:
    """
    Class for srt utilities
    """

    def __init__(self,
                 id,
                 path = None,
                 comment = '##',
                 set_id_as_prog = True,
                 validate = True):
        self.id = id
        self.read(path,
                  comment = comment,
                  set_id_as_prog = True,
                  validate = True)

    def read(self,
             path = None,
             comment = '##',
             set_id_as_prog = True,
             validate = True):
        """ 
        Read and parse an .srt 
        """
        # read all the lines and put them in a list
        with open(path, 'r') as f:
            self.lines = f.readlines()
        # rm all the lines starting with comments
        ptrn = '^' + str(comment)

        
    def write(self, path):
        pass

    def print(self):
        pass

    def stats(self):
        pass

    def split(self):
        pass


a = srt("id", "/tmp/asd")    
b = open("/tmp/asd")
b.close()
