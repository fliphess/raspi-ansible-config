use Byte::Log;
my $log = new Byte::Log();
$log->class('dbigration/activation/database backup/....');
$log->tag('cancelled/requested/started/finished');
$log->source('quickscan/sevicepanel/...');
$log->log($domain,"this happened");
