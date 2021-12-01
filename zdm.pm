package zdm;
require Exporter;
@ISA = qw(Exporter);
@EXPORT = qw(htmlhead htmlfoot sendmail);
@EXPORT_OK = qw($orderfile $logfile $fieldbreake $linebreake $htmlbreake $textbreake $mailheader $styleorder $stylemail);
{
$sitesfile = 'sites.dat';
$bannersfile = 'banners.dat';
$polygraphyfile = 'polygraphy.dat';
$projectsfile = 'projects.dat';
$orderfile = 'order';
$logfile = 'stat';
$passfile = 'pass.dat';
$newsfile = 'news.dat';
$pricesfile = 'prices.dat';
$passbreake = '===';
$fieldbreake = 'A2dk75';
$linebreake = 'lb76Az';
$htmlbreake = '<br>';
$textbreake = '\r\n';
$mailheader = 'Content-Type: text/html; charset=Windows-1251'.(chr 10).'Content-Transfer-Encoding: 8bit'.(chr 10).(chr 10).'<html>'.(chr 10);
$stylemail = "<style>.newstext{font-size: 12px;font-family: Verdana, Geneva, Arial, Helvetica, sans-serif;font-weight : bold;font : bold 12px Verdana, Geneva, Arial, Helvetica, sans-serif;color : \#646F7A;}</style>".(chr 10)."<body bgcolor='\#89C2F9'>";

sub htmlhead($$)
{
 print "Content-type: text/html\n\n";
	print "<html>\n";
	print "<head>\n";
	print "<meta http-equiv='Content-Type' content='text/html; charset=windows-1251'>\n";
	print "<title>Avila.$_[0].</title>\n";
	print "</head>\n";
	print "<script language='JavaScript' src='top.js'></script>\n";
	print "<script>header('$_[1]')</script>\n";
	print "<td colspan='2' align='center'>\n";
};
sub htmlfoot($)
{
 print "</td>\n";
 print "</tr>\n";
 print "<tr><script>document.write(\"<td height='\"+(my-150-35-$_[0])+\"'>\")</script></td></tr>\n";
 print "<tr><td></td><td align='right' class='currentdate'>|<a href=\#pagetop onClick='scrollTo(0,0); return false;'><font color='\#BACBDB'> вверх страницы </font></a>|</td></tr>\n";
 print "<script language='JavaScript' src='bottom.js'></script>\n";
 print "</html>\n";
};
sub sendmail($$$$)
{
 open (MAIL, "| /usr/sbin/sendmail $_[0]");
 print MAIL "from:$_[1]\n";
 print MAIL "subject:$_[2]\n";
 print MAIL $_[3],"\n";
 close (MAIL);
}
}
