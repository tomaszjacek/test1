use AI::Genetic::Pro;
 


 %data = ('red', 0.34, 'blue', 0.1, 'Kumar', 0.1 ,'big',0.34,'medium',0.1,'small',0.1,'very_fat',0.1, 'fat',0.01,'fit',0.34,'thin',0.1,'very_thin',0.1);

sub fitness {
    my ($ga, $chromosome) = @_;
    my @tmp = @{$ga->as_array($chromosome)};
    my $n = @tmp;
    my $out=0;
    if(($tmp[0] eq "red") || ($tmp[1] eq "big") || ($tmp[2] eq "fit")){
          $out=$data{$tmp[0]}+$data{$tmp[1]}+$data{$tmp[2]};
        }else{
          $out=($data{$tmp[0]}*0.1)+($data{$tmp[1]}*0.1)+($data{$tmp[2]}*0.1);
    }

    if($n!=3){$out=0;}
    print "@tmp $out\n";
    return $out; 
}
 
sub terminate {
    my ($ga) = @_;
    my $result = $ga->as_value($ga->getFittest);
    
    print "TERMINATE $result\n";
    if($result>1){
    return 1;
    }else{
        return 0;
    }
}
 
my $ga = AI::Genetic::Pro->new(        
    -fitness         => \&fitness,        # fitness function
    -terminate       => \&terminate,      # terminate function
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
     
# init population of 32-bit vectors
$ga->init([
           [qw/red blue green/],
           [qw/big medium small/],
           [qw/very_fat fat fit thin very_thin/],
          ]);

  
# evolve 20 generations
$ga->evolve(20);
 
# best score
print "SCORE: ", $ga->as_value($ga->getFittest_as_arrayref), ".\n";
print "VALUE: ", $ga->as_string($ga->getFittest_as_arrayref), ".\n";


