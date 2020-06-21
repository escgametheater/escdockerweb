FROM php:7.2-apache
ADD 001-catchall.conf /etc/apache2/sites-enabled/001-catchall.conf
RUN a2enmod rewrite
RUN a2enmod headers
RUN a2enmod ssl
RUN a2enmod http2
RUN a2enmod vhost_alias

#RUN a2enmod proxy
#RUN a2enmod proxy_fcgi

RUN rm -rf /etc/apache2/sites-enabled/000-default.conf
# RUN rm -rf /var/www/html; ln -s /home/escweb/apps/www/webroot /var/www/html;
RUN mkdir /var/escweb; mkdir /var/escweb/media; mkdir /var/escweb/uploads; mkdir /var/escweb/log; mkdir /var/escweb/cache; mkdir /var/escweb/cache/www; mkdir /var/escweb/cache/api; mkdir /var/escweb/templates; mkdir /var/escweb/templates/www; mkdir /var/escweb/templates/api; mkdir /var/cache/nginx/controller_assets; mkdir /var/cache/nginx/esc
RUN touch /var/escweb/log/error.log
RUN chmod -R 777 /var/escweb/*
RUN apt-get update && apt-get install -y \
        libpq-dev \
        nano \
	    curl \
	    zlib1g-dev  \
	    libxml2-dev \
	    imagemagick \
	    libmagickwand-dev \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install mysqli \
    && docker-php-ext-install zip \
    && docker-php-ext-install xml \
    && docker-php-ext-install bcmath \
    && pecl install imagick-3.4.3 \
    && pecl install redis-4.0.1 \
    && pecl install apcu-5.1.11 \
    && docker-php-ext-enable imagick \
    && docker-php-ext-enable redis \
    && docker-php-ext-enable apcu \
    && docker-php-ext-enable zip \
    && docker-php-ext-enable xml \
    && docker-php-ext-install pcntl \
    && docker-php-ext-install sockets