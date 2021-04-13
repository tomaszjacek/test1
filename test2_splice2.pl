
my $chromosomA = [
          [1, 2, 3, 4, 5],
          [11, 22, 33,  44, 55],
          [111, 222, 333,  444, 555],
          [1111, 2222, 3333,  4444, 5555],
        ];

my $chromosomB = [
          [7, 8, 9],
          [77,88,99],
          [777,888,999],
          [7777,8888,9999],
        ];




#@elders = map { $chromosomes->[$_]->clone } @elders;
my @elders=();
push(@elders,$chromosomA);
push(@elders,$chromosomB);

printChromosom($chromosomA);
printChromosom($chromosomB);

my @newChromosom=();
for my $genGroup (0 .. $#{$chromosomA}){
  my @points = liczMiejscaCO($chromosomA->[$genGroup],$chromosomB->[$genGroup]);
  for my $pt (@points){
	  #print "A: @{$chromosomA->[$genGroup]}\n";
    #print "B: @{$chromosomB->[$genGroup]}\n";
	  splice @{$chromosomB->[$genGroup]}, 0, $pt, splice( @{$chromosomA->[$genGroup]}, 0, $pt, @{$chromosomB->[$genGroup]}[0..$pt-1] );
    #print "AA: @{$chromosomA->[$genGroup]}\n";
    #print "BB: @{$chromosomB->[$genGroup]}\n";
    #push(@newChromosom, \@tmp);
	  #0;
      
  }
}
print "\n","-" x 73,"\n";

printChromosom($chromosomA);
printChromosom($chromosomB);

sub liczMiejscaCO{
  my $tableAref=shift;
  my $tableBref=shift;
  my $lengthA = scalar @$tableAref;
  my $lengthB = scalar @$tableBref;
  my $min = 0;
  my $max = 0;
  if($lengthA>$lengthB){
    $max=$lengthB;
  }else{
    $max=$lengthA;
  }
  my @points;

  if($min < $max and $max - $min > 2){
	  my $range = $max - $min;
	  @points = map { $min + int(rand $range) } 1..2;
  }
  print "points @points\n";
  return @points;
}


sub printChromosom{
  my $chrRef = shift;
  print "\n","-" x 72,"\n";
  foreach my $it (@{$chrRef}){
    print "@{$it}\n";

  }
 print "-" x 72,"\n";
}


=head2
my @tablicaA = (0..19);
my @tablicaB = ( A..M);
print "@tablicaA\n@tablicaB\n";
@replaced = splice(@tablicaA,5,scalar( @tablicaB ),@tablicaB);
print "\n","-" x 72,"\n";
print "@tablicaA\n@tablicaB\n@replaced\n";
print "\n","-" x 72,"\n";
my @tablicaA = (0..19);
my @tablicaB = ( A..M);
@replaced = splice(@tablicaA,scalar(@tablicaA)-2,2,@tablicaB[6..7]);
print "@tablicaA\n@tablicaB\n@replaced\n";
=cut

=head1
my $chromosomA = [
          [1, 2, 3, 4, 5],
          [11, 22, 33,  44, 55],
          [111, 222, 333,  444, 555],
          [1111, 2222, 3333,  4444, 5555],
        ];

my $chromosomB = [
          [7, 8, 9],
          [77,88,99],
          [777,888,999],
          [7777,8888,9999],
        ];


my @points;
my $min = 1;
my $max = 3;
if($min < $max and $max - $min > 2){
	my $range = $max - $min;
	@points = map { $min + int(rand $range) } 1..2;
}
print "points @points\n";

#@elders = map { $chromosomes->[$_]->clone } @elders;
my @elders=();
push(@elders,$chromosomA);
push(@elders,$chromosomB);

printChromosom($chromosomA);
printChromosom($chromosomB);

for my $pt (@points){
	@elders = sort {
	splice @$b, 0, $pt, splice( @$a, 0, $pt, @$b[0..$pt-1] );
	0;
    } @elders;
}

print "\n","-" x 72,"\n";

printChromosom($elders[0]);
printChromosom($elders[1]);


sub printChromosom{
  my $chrRef = shift;
  print "\n","-" x 72,"\n";
  foreach my $it (@{$chrRef}){
    print "@{$it}\n";

  }
 print "-" x 72,"\n";
}



=cut























#my $elders="***";
#my @elders = unpack 'I*', $elders;
#print "@elders\n";