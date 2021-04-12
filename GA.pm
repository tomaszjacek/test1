package GA;

use vars qw($VERSION);

$VERSION = 1.005;
#---------------

use warnings;
use strict;
use base 							qw( Class::Accessor::Fast::XS );
#-----------------------------------------------------------------------
use Carp;
use Clone 							qw( clone );
use Struct::Compare;
use Digest::MD5 					qw( md5_hex );
use List::Util 						qw( sum );
use List::MoreUtils 				qw( minmax first_index apply );
#use Data::Dumper; 					$Data::Dumper::Sortkeys = 1;
use Tie::Array::Packed;
use UNIVERSAL::require;
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
__PACKAGE__->mk_accessors(qw(
	mce
	type
	population
	terminate
	chromosomes 
	crossover 
	native
	parents 		_parents 
	history 		_history
	fitness 		_fitness 		_fitness_real
	cache
	mutation 		_mutator
	strategy 		_strategist
	selection 		_selector 
	_translations
	generation
	preserve		
	variable_length
	_fix_range
	_package
	_length
	strict			_strict
	workers
	size
	_init
));
#=======================================================================
# Additional modules
use constant STORABLE	=> 'Storable';
use constant GD 		=> 'GD::Graph::linespoints'; 
#=======================================================================
my $_Cache = { };
my $_temp_chromosome;
#=======================================================================
sub new {
	my ( $class, %args ) = ( shift, @_ );
	
	#-------------------------------------------------------------------
	my %opts = map { if(ref $_){$_}else{ /^-?(.*)$/o; $1 }} @_;
	my $self = bless \%opts, $class;
	
	#-------------------------------------------------------------------

	
	#-------------------------------------------------------------------
	$self->_set_strict if $self->strict;

	#-------------------------------------------------------------------
	return $self;


}

sub printParameters {
	my ($self) = @_;
	
	print "mce ". $self->mce . "\n";
    print "type ". $self->type . "\n";
}

1;