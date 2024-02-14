file { '/var/www/html/wp-settings.php':
  ensure => file,
}

exec { 'replace_line':
  command => "grep -q 'phpp' /var/www/html/wp-settings.php && sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/bin:/usr/bin',
  require => File['/var/www/html/wp-settings.php'],
}
