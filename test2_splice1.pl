my $chromosom = [
          [1, 2, 3, 4, 5],
          [11, 22, 33,  44, 55],
          [111, 222, 333,  444, 555],
          [1111, 2222, 3333,  4444, 5555],
        ];




my @points;
my $min = 1;
my $max = 5;
if($min < $max and $max - $min > 2){
	my $range = $max - $min;
	@points = map { $min + int(rand $range) } 1..2;
}
print "points @points\n";

#@elders = map { $chromosomes->[$_]->clone } @elders;
my @elders=();
push(@elders,$chromosom->[0]);
push(@elders,$chromosom->[1]);
push(@elders,$chromosom->[2]);
push(@elders,$chromosom->[3]);

print "@{$elders[0]}\n";
print "@{$elders[1]}\n";
print "@{$elders[2]}\n";
print "@{$elders[3]}\n";
for my $pt(@points){
	@elders = sort {
	splice @$b, 0, $pt, splice( @$a, 0, $pt, @$b[0..$pt-1] );
	0;
    } @elders;
}

print "\n","-" x 72,"\n";
print "@{$elders[0]}\n";
print "@{$elders[1]}\n";
print "@{$elders[2]}\n";
print "@{$elders[3]}\n";






























#my $elders="***";
#my @elders = unpack 'I*', $elders;
#print "@elders\n";