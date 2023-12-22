# install flask with pip3
class { 'python':
   version => '3',
}

python::pip { 'flask':
   ensure    => '2.1.0',
   provider  => 'pip3',
}
