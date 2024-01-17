# A puppet script to replace error file on server

$error_file = '/var/www/html/wp-settings.php'

#replace line containing "phpp" with "php"

exec { 'fix error file':
  command => "sed -i 's/phpp/php/g' ${error_file}",
  path    => ['/bin','/usr/bin']
}
