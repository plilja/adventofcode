
my %m = (
    '(' => 1,
    ')' => -1,
);

for $*IN.lines() -> $line {
    my $sum = 0;
    for (split('', $line)) -> $c {
        if (%m{$c}) {
            $sum += %m{$c};
        }
    }
    say $sum;
}
