my $sum = 0;

for $*IN.lines() -> $line {
    my @dim = split('x', $line).map({$_.Int});
    my $l = @dim[0];
    my $w = @dim[1];
    my $h = @dim[2];
    $sum += 2 * ($l*$w + $w*$h + $h*$l);
    $sum += min ($l*$w, $w*$h, $h*$l);
}
say $sum;
