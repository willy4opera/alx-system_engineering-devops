# A puppet script to replace error file on server

$Error_File = '/var/www/html/wp-settings.php'

#replace line containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${Error_File}",
  path    => ['/bin','/usr/bin']
}
