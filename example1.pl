use strict;
use Statistics::Basic;

my $chromosom = [
          [1.500, 1.250, 0.750, 0.500, 0.250, 0.000],
          [2.663, -0.164, -1.090,  1.746, -0.162, -0.218],
          [-0.463, -0.504, -0.702,  1.447, -1.464,  0.071]
        ];


my %genotyp=();
my %fenotyp=();

while (my $line = <DATA>) {$line =~ s/\r?\n\z//;
    my @splited = split(/ /, $line);
    my $id = shift(@splited);
    my $fenotyp = pop(@splited);
    #kazdy osobnik ma zapisana tablice genotypow
    $genotyp{$id}=\@splited;
    #i wartosc fenotypu
    $fenotyp{$id}=$fenotyp;
}


foreach my $id (keys %genotyp){
  print "wartoscGenotypu osobnika $id = ". liczWartoscGenotypu($id) . " | jego genotyp @{$genotyp{$id}}" . "\n";# | jego fenotyp :$fenotyp{$id}|\n";
}

print "dopasowanie chromosomu " . fitness($chromosom) . "\n";




sub liczWartoscGenotypu{
    my $id = shift;

    my $wartoscGenotypu = 0;
    my $liczbaGenow = scalar(@{$genotyp{$id}});
    for (my $n = 0 ;$n<$liczbaGenow;$n++){
        #wartosc danego genu jest odczytywana z kolumny odpowiadajacej kolejnosci genow i z wiersza zaleznie od wartosci genu (0 1 2).
        $wartoscGenotypu += $chromosom->[$genotyp{$id}[$n]][$n];
    }
    #print "$id $wartoscGenotypu | @{$genotyp{$id}} |$fenotyp{$id}|\n";

    return $wartoscGenotypu;
}

sub fitness{
   my $chr = shift;

   my $korelacja = 0;
   my @tablicaFenotypow = ();
   my @tablicaWartosciGenotypow = ();
   foreach my $id (keys %genotyp){
       push(@tablicaFenotypow, $fenotyp{$id});
       push(@tablicaWartosciGenotypow, liczWartoscGenotypu($id));
   }
 
   my $korelacja = Statistics::Basic::corr(\@tablicaFenotypow,\@tablicaWartosciGenotypow);

  return $korelacja;
}
#idName gen1 gen2 gen3 gen4 gen5 gen6 fenotyp

__DATA__
ID1 0 0 1 0 2 2 150
ID2 0 0 0 0 0 0 160
ID3 1 1 2 1 0 2 110
