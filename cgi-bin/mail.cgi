#!/usr/bin/perl

@query_strings = split("&", $ENV{"QUERY_STRING"});
foreach $q (@query_strings) {
        ($attr, $val) = split("=", $q);
        $query{$attr} = $val;
        }
$sendto = $query{'to'};
open (MAIL, "| /usr/sbin/sendmail $sendto");
print MAIL "from:zag.virtualave.net\n";
print MAIL "subject:",$query{'subj'},"\n";
print MAIL $query{'mess'},"\n";
close (MAIL);

