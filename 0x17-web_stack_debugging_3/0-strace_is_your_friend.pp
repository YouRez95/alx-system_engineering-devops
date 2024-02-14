# fix the phpp extension in wp-setting
exec { 'replace_phpp':
  command  => "grep -q 'phpp' /var/www/html/wp-settings.php && sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  provider => 'shell',
}
