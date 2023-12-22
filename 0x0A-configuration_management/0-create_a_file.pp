# create a file in /tmp

file { 'school':
       ensure  => 'present',
       content => 'I love Puppet',
       owner   => 'www-data',
       mode    => '0744',
       group   => 'www-data',
       path    => '/tmp/school',
}
