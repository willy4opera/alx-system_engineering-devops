# A puppet manuscript to replace a line in a file on a server

$Error_File = '/var/www/html/wp-settings.php'

#Fix Error File containing "phpp" with "php"

exec { 'Fix Error File':
  command => "sed -i 's/phpp/php/g' ${Error_File}",
  path    => ['/bin','/usr/bin']
}
