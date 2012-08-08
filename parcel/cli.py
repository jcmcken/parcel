from enhanced_argparse import EnhancedArgumentParser as EAP

def create_cli():
    main = EAP(prog='par')




    cli = optparse.OptionParser()
    cli.add_option('-b', '--begin-packing', action='store_true',
        help='Start creating a dynamic manifest')
    cli.add_option('-p', '--pack', action='store_true',
        help='Finish packing the current dynamic manifest')
    cli.add_option('-O', '--output',
        help='Parcel output file name')
    cli.add_option('-a', '--add')
    cli.add_option('-d', '--del')
    cli.add_option('-c', '--clear', action='store_true',
        help='Clear the current dynamic manifest')
    cli.add_option('-f', '--from-config',
        help='Pack a parcel from a configuration file')
    cli.add_option('-u', '--unpack', metavar='PARCEL',
        help='Unpack the contents of PARCEL')
    cli.add_option('-C', '--change-dir', metavar='DIR',
        help='Unpack with respect to DIR rather than /')
    cli.add_option('-n', '--no-op', action='store_true',
        help='Pretend to unpack')
    cli.add_option('-l', '--log-level',
        help='set the log level (defaults to INFO)')
    cli.add_option('--validate', metavar='PARCEL',
        help='validate all files listed in PARCEL match the current system')


    
