# Puppet manifest to automate debugging of Apache 500 Internal Server Error

# Install strace package
package { 'strace':
  ensure => installed,
}

# Define exec resource to run strace
exec { 'debug_apache':
  command   => 'strace -p 168181',
  path      => '/usr/bin:/bin',
  logoutput => true,
  require   => Package['strace'],
}

# Define exec resource to reproduce the issue with curl
exec { 'curl_localhost':
  command   => 'curl -sI 127.0.0.1',
  path      => '/usr/bin:/bin',
  logoutput => true,
  require   => Exec['debug_apache'],
}
