FROM hhvm/hhvm:3.30.0
ADD php.ini /etc/hhvm/php.ini
ADD server.ini /etc/hhvm/server.ini
RUN mkdir /var/escweb; mkdir /var/escweb/media; mkdir /var/escweb/uploads; mkdir /var/escweb/log; mkdir /var/escweb/cache; mkdir /var/escweb/cache/www; mkdir /var/escweb/cache/api; mkdir /var/escweb/templates; mkdir /var/escweb/templates/www; mkdir /var/escweb/templates/api;
RUN touch /var/escweb/log/error.log
CMD ["hhvm", "-m", "server", "-vServer.Type=fastcgi", "-vServer.Port=9010", "-vMysql.Connect_timeout=180000", "-c","/etc/hhvm/server.ini", "--debug-sandbox=default", "-vServer.AllowRunAsRoot=1"]