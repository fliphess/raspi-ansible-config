package Byte::Class;

## @class Byte::Class;
# 
# @brief Does whit and that
#
# This class is ...[long description follows]
sub new {
	my $proto = shift;
	my $class = ref($proto) || $proto;
	
	my $self = bless {}, $class;
        #for subclass:
        #my $self = $class->SUPER::new(@_);
        
        return $self;
}
