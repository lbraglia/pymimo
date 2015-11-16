import argparse

def argparser(opts):
    'Helper function for argument parsing.'
    parser = argparse.ArgumentParser()
    defaults = {}
    for i in opts:
        optname = i[0]
        optdescription = i[1]
        optdefault = i[2]
        opttype = i[3]
        # crea
        help_string = '{0} (default: {1})'.format(optdescription, optdefault)
        parser.add_argument('--' + optname, help = help_string, type = opttype)
    # esegui il parser e ottieni i valori
    args = vars(parser.parse_args()) #vars to change to a dict
    # per ogni linea in opts
    for i in opts:
        optname = i[0]
        optdescription = i[1]
        optdefault = i[2]
        opttype = i[3]
        # se il valore è a none in args impostalo al valore di default
        # specificato
        if (args[optname] is None):
            args[optname] = optdefault
        # se il tipo è logico sostituisci un valore possibile true con
        # l'equivalente python
        if (opttype == bool):
            true_values = ('true', 'True', 'TRUE', 't', 'T', '1', 'y', 'Y',
                           'yes', 'Yes', 'YES') 
            if (args[optname] in true_values):
                args[optname] = 'True'
            else:
                args[optname] = 'False'
        # converti il tipo a quello specificato
        args[optname] = opttype(args[optname])
    return(args)


def do_tests():
    opts = (
        # (param, help, default, returned type)
        ('setup', 'setup host\'s software', 'False', str),
        ('update', 'update host\'s software', 'False', str),
    )
    args = argparser(opts)
    print(args)


if __name__ == '__main__':
    do_tests()
