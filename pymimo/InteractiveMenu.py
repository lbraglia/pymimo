import readline
readline.parse_and_bind('set editing-mode emacs')


class InteractiveMenu():
    """
    Class used to receive user input given a multiple choiche menu
    """
    
    def __init__(self, choices,
                 title = None,
                 multiple = False,
                 rval = True,
                 strict = False):
        
        choices = tuple(choices)
        return

if False:    #interactive tests
    choices = ['a', 'b', 'c']
    choices = InteractiveMenu(choices)
    print(choices)
