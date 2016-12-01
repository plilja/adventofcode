#!/usr/bin/perl6

my %prices = (  '(' => 1,
                ')' => -1,
             );

my $input = prompt "Input file: ";
my $fh = open "$input", :r;
my $parens = $fh.slurp-rest;
$fh.close;
#my @chars = split( '', $parens);
my @chars = $parens.split( '' );
my $char;
my $sum = 0;
for @chars -> $char {
    if (any(%prices.keys) eq "$char") {
        $sum += %prices{$char};}
    else{
        say "nope $char";
    }
}
say "sum total: $sum";
