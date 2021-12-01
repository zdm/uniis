#!/usr/bin/perl

use CGI;

$ip = $ENV{'REMOTE_ADDR'};
$browser = $ENV{'HTTP_USER_AGENT'};

@query_strings = split("&", $ENV{"QUERY_STRING"});
foreach $q (@query_strings) {
        ($attr, $val) = split("=", $q);
        $query{$attr} = $val;
        }

if ($query{'id'} == 2) {$logfile = "rate.log";}
elsif ($query{'id'} == 3) {$logfile = "button.log";}
else {$logfile = "stat.log";}

if (! (-f "$logfile")) {
        open (LOG, ">$logfile");
        close LOG;
        }

($csec,$cmin,$chour,$cmday,$cmon,$cyear,$cwday,$cyday,$cisdst) =localtime(time);
$cyear=$cyear+1900;
$cmon=$cmon+1; 

open (LOG,">>$logfile");
print LOG "$cmday.$cmon.$cyear - $chour:$cmin:$csec - $ip - $browser";

if ($query{'id'}==2) {print LOG " - $query{'estimate'}\n";}
elsif ($query{'id'}==3) {print LOG " - $query{'button'}\n";}
else {print LOG "\n";}

close LOG;




