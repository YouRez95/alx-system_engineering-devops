# install flask with pip3
class { 'python':
   version => '3',
}

python::pip { 'Flask':
   ensure    => '2.1.0',
   provider  => 'pip3',
}
