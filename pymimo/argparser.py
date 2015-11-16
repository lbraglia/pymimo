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
        # create help string and add argument to parsing
        help_string = '{0} (default: {1})'.format(optdescription,
                                                  str(optdefault))
        parser.add_argument('--' + optname, help = help_string, type = str)
    # do parsing
    args = vars(parser.parse_args()) #vars to change to a dict
    # defaults settings and types management
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


def test(opts):
    args = argparser(opts)
    for key in sorted(args):
            print "%s: %s" % (key, args[key])

if __name__ == '__main__':

    opts = (
        # (param, help, default, returned type)
        ('setup', 'setup host\'s software', 'False', str),
        ('update', 'update host\'s software', 'False', str),
    )
    test(opts)

    opts = (
        ('download', 'download files?', True, bool),
        ('preprocess', 'preprocess downloaded files?', False, bool),
        ('years', 'years to be downloaded (PagesList)', 'last available', str),
        ('eds', 'edition/s to be downloaded (comma separated)', 'SE,SSE', str),
        ('rawdir', 'dir where to save raw data', './jcr_data', str),
        ('cleandir', 'dir where to save cleaned data', './jcr_data', str),
        ('overwrite', 'download again already downloaded files?','False', str),
        ('quiet', 'turn off verbosity', 'False', str)
    )
    test(opts)


