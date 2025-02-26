# This manifest fixes the `phpp` extensions in the WordPress file `wp-settings.php` to `php`.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
