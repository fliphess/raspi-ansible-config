use Getopt::Long;

###
# Get Options
###

my $verbose     = -t STDIN ? 2 : 0;
my $interactive = -t STDIN;
my $help        = 0;
my $dryrun      = 0;

my $result = GetOptions(
	"verbose|v" => sub { $verbose++ },
	"quiet|q"   => sub { $verbose-- },
	'dry-run'   => \$dryrun,
	'help|h'    => \$help, 
);

sub usage {
	my $msg = shift || '';

	print <<"        END";
        Usage:
         $0 [-v] [-h]

        Example:
         $0

             --dry-run   - do not change anything
         -v, --verbose   - print more messages 
         -h, --help      - display usage
        END
	log_critical $msg if $msg;
	exit 1;
}

usage if not $result;
usage if $help;
log_set_verbose $verbose;
