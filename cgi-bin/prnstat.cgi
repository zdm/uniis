#!/usr/bin/perl

print "Content-type: text/html\n\n";
print "<html>";
open (LOG, "<stat.log");
print "<center><H2>Statistics</H2></center>";
while (not eof (LOG)){
        $a=<LOG>;
        print "$a<br>";
        };
close LOG;

open (LOG, "<button.log");
print "<center><H2>Button</H2></center>";
($lst[1],$lst[2],$lst[3],$lst[4],$lst[5],$lst[6],$lst[7],$lst[8],$lst[9])=(0,0,0,0,0,0,0,0,0);
$bt = 0;
while (not eof (LOG)){
        $a=<LOG>;
        @b = split(" - ", $a);
        $lst[$b[4]]++; $bt++;
        print "$a<br>";
        };
print "ќбщее количество нажатий на кнопки = ", $bt, "<br>";
for ($i = 1; $i < 10; ++$i){
        print $i, " - ", 100 * $lst[$i] / $bt;
        print "<br>";
        }
           
close LOG;

open (LOG, "<rate.log");
print "<center><H2>Rate</H2></center>";
$sum = 0; $i = 0;
while (not eof (LOG)){
        $a=<LOG>;
        @b = split(" - ", $a);
        $sum = $sum + $b[4]; $i++;
        print "$a<br>";
        };
print "—редн€€ оценка сайта = ", $sum/$i;
close LOG;

print "</html>\n";









