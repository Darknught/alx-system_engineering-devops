# Install Nginx web server (w/ Puppet)
package { 'nginx':
  ensure => installed,
}

file_line { '/etc/nginx/sites-available/default':
  ensure => present,
  content => server {
    listen 80 default_server;
    listen [::]:80 default_server;

    add_header X-Served-By $hostname;
    root /var/www/html;
    index index.html index.htm;
    }
}

file { '/var/www/html/index/html':
  content => 'Hello World',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
