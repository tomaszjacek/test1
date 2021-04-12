package Individual;

use GeneticProgram;

# the PerlGP library is distributed under the GNU General Public License
# all software based on it must also be distributed under the same terms

@ISA = qw(GeneticProgram);

sub _init {
  my ($self, %p) = @_;

  my %defaults = ( MinTreeNodes => 20,
		   NodeMutationProb => 1/200,
		   NodeXoverProb => 1/100,
		   NumericMutationFrac => 0.1,
		   NumericAllowNTypes => { DENOM=>2, NUMX=>0.1 },
		 );

  $self->SUPER::_init(%defaults, %p);
}

sub pdiv {
  return $_[1] ? $_[0]/$_[1] : $_[0];
}

sub ppow {
  my ($x, $p) = @_;
  $p = 30 if ($p>30);
  $p = -30 if ($p<-30);
  $p = int($p) if ($x<0);
  return $x**$p;
}

sub extraLogInfo {
  my $self = shift;
  return sprintf "mut %-12.6g xover %-12.6g",
    $self->NodeMutationProb(), $self->NodeXoverProb();
}

1;
