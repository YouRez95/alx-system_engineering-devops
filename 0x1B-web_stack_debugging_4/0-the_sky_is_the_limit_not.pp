#fix nginx to serve more requests

file {'modify ULIMIT':
  ensure  => file,
  path    => '/etc/default/nginx',
  content => 'ULIMIT="-n 1000000"'
}

service { 'nginx':
  ensure     => running,
  name       => 'nginx',
  hasrestart => true,
  subscibe   => File['/etc/default/nginx']
}
