
my %m = (
    '(' => 1,
    ')' => -1,
    '[' => 10,
    ']' => -10,
    '{' => 100,
    '}' => -100,
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
