#!/usr/bin/perl

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
BEGIN {
	#-------------------------------------------------------------------
	use FindBin	qw( $RealBin $Script );
	use lib $RealBin . q[/../lib/perl];
	#-------------------------------------------------------------------
	chdir $RealBin;
}
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

use warnings;
use strict;
#-----------------------------------------------------------------------
use AI::Genetic::Pro;
use List::Util				qw( sum );
use Data::Dumper; 			$Data::Dumper::Sortkeys = 1;
use Statistics::Basic;
#=======================================================================
=bck Niepoprawne. Oba wektory podawane do corr musza byc tej samej dlugosci.
sub fitness {
	my ( $ga, $chr ) = @_;

	my @gen = $ga->as_array( $chr );
	my @fen = pop @gen;
	my $ret = Statistics::Basic::corr( \@fen, \@gen );	

	return $ret || 0;
}
=cut
#=======================================================================
# Losowa wartosc, bo populacja rozwija sie calkowicie losowo
sub fitness {
	my ( $ga, $chr ) = @_;
	
	return int( rand 9999 );
}
#=======================================================================
my $ga = AI::Genetic::Pro->new(        
    -fitness         => \&fitness,         # fitness function
    #-terminate       => \&terminate,      # terminate function
    -type            => 'listvector',      # type of chromosomes
    -population      => 100,     	       # population
    -crossover       => 0.9,               # probab. of crossover
    -mutation        => 0.01,              # probab. of mutation
    -parents         => 2,                 # number  of parents
    -selection       => [ 'Roulette' ],    # selection strategy
    -strategy        => [ 'Points', 2 ],   # crossover strategy
#    -cache           => 1,                # cache results
#    -history         => 1,                # remember best results
	-native			 => 1,				   # native arrays				# Wyglada, ze pojawil sie blad w Tie::Array::Packed. Jeszcze musze to sprawdzic, ale na razie wersja natywna jest OK.
    -preserve        => 3,                 # remember the bests
    -variable_length => 0,                 # turn variable length ON
    #-mce             => 0,                # optional MCE support		# Za mala populacja i za prosta funkcja fitness 
    #-workers         => 1,                # number of workers (MCE)	# Za mala populacja i za prosta funkcja fitness
);
#-----------------------------------------------------------------------
# Inicjujemy populacje 100. osobnikow o genach zgodnych z ponizszymi wartosciami
$ga->init(
	[
		[ 1.500,  2.663, -0.463 ],	# Genotypy. Kazdy z 6. genow moze przyjac 3 rozne wartosci
		[ 1.250, -0.164, -0.504 ],
		[ 0.750, -1.090, -0.702 ],
		[ 0.500,  1.746,  1.447 ],
		[ 0.250, -0.162, -1.464 ],
		[ 0.000, -0.218,  0.071 ],
	#	[ 150,	  160,	  110	],	# Tenotypy Teraz z tego nie korzystam, bo nie wiem, jak to wyznaczyc dla wiekszej liczby genotypow
	]
);
#-----------------------------------------------------------------------
# Ewolucja krokowa. Oceniamy po kazdym kroku cala populacje. W takim przypadku nie mamy mozliwosci nadania kierunku ewolucji, bo nie wskazujemy, ktory osobnik jest dla nas lepszy (umiemy to okreslic tylko dla calej populacji?)
for( 1 .. 5 ){
	print "\n", "-" x 72, "\n";
	print "Generacja: $_\n\n";
	
	$ga->evolve( 1 );
	
	my $arr = $ga->chromosomes;
	for my $chr ( @$arr ){
		my @ary = $ga->as_array( $chr );
		print map { sprintf( "%03.3f\t", $_ ) } @ary;
		print " => ", sum( @ary ), "\n";
	}
}
#=======================================================================
exit 0;
