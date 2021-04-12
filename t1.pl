use lib "/media/sf_shared/nostromoPerl_v2/";
use GA;

my $ga = GA->new(        
#    -fitness         => \&fitness,        # fitness function
#    -terminate       => \&terminate,      # terminate function
    -type            => 'listvector',      # type of chromosomes
    -population      => 10,             # population
    -crossover       => 0.9,              # probab. of crossover
    -mutation        => 0.01,             # probab. of mutation
    -parents         => 2,                # number  of parents
    -selection       => [ 'Roulette' ],   # selection strategy
    -strategy        => [ 'Points', 2 ],  # crossover strategy
    -cache           => 0,                # cache results
    -history         => 1,                # remember best results
    -preserve        => 3,                # remember the bests
    -variable_length => 1,                # turn variable length ON
    -mce             => 1,                # optional MCE support
    -workers         => 1,                # number of workers (MCE)
);



print $ga->printParameters . "\n";




sub get_package_by_element_size {
	return if $Native;
	
	my $size = shift;
	
	my $type =	#$size <			   32	? undef										:	#  Pure Perl array
				#$size <			   32	? 'AI::Genetic::Pro::Array::Tied'			:	#  Pure Perl array
			 	$size <     		  128	? 'Tie::Array::Packed::Char'				: 	#  8 bits
				$size <     		  256	? 'Tie::Array::Packed::UnsignedChar'		:	#  8 bits
				$size <  		   65_537	? 'Tie::Array::Packed::ShortNative'			:	# 16 bits
				$size < 		  131_073	? 'Tie::Array::Packed::UnsignedShortNative'	:	# 16 bits
				$size < 	2_147_483_648	? 'Tie::Array::Packed::Integer'				:	# 32 bits
				$size < 	4_294_967_297	? 'Tie::Array::Packed::UnsignedInteger'		:	# 32 bits; MAX
				undef;
				
	return unless $type;
	return $type;
}

$size =70_000;
print "typ dla $size to " .get_package_by_element_size($size) . "\n";

=head1
use List::Util qw(shuffle first);
use List::MoreUtils qw(first_index);


$length = 2;
$data = [
           [1, 5],
           [0, 20],
           [4, 9],
          ];

@genes = map { $_->[1] + int rand($_->[2] - $_->[1] + 1) } @$data[0..$length];

print "\n" . "-" x 73 . "\n";
print "@genes" ."\n";

print "\n" . "-" x 73 . "\n";

@genes = map { rand > 0.5 ? 1 : 0 } 0..$length;
print "@genes\n";

print "\n" . "-" x 73 . "\n";



@genes = shuffle 0..$length;
print "@genes\n";

print "\n" . "-" x 73 . "\n";

=cut

