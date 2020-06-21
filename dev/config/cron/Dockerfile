FROM php:7.2-fpm
ADD process-sms-queue.sh /process-sms-queue.sh
ADD clean-instances.sh /clean-instances.sh
ADD hourly-scripts.sh /hourly-scripts.sh
ADD daily-scripts.sh /daily-scripts.sh

RUN chmod 0755 /process-sms-queue.sh
RUN chmod 0755 /clean-instances.sh
RUN chmod 0755 /hourly-scripts.sh
RUN chmod 0755 /daily-scripts.sh
RUN mkdir /var/escweb; mkdir /var/escweb/media; mkdir /var/escweb/uploads; mkdir /var/escweb/log; mkdir /var/escweb/cache; mkdir /var/escweb/templates;
RUN touch /var/escweb/log/error.log
RUN chmod -R 777 /var/escweb/*
RUN apt-get update && apt-get install -y \
        cron \
        imagemagick \
        libmagickwand-dev \
        nano \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install mysqli \
    && docker-php-ext-install bcmath \
    && pecl install redis-4.0.1 \
    && pecl install apcu-5.1.11 \
    && pecl install imagick-3.4.3 \
    && docker-php-ext-enable imagick \
    && docker-php-ext-enable redis \
    && docker-php-ext-enable apcu \
    && docker-php-ext-install pcntl \
    && docker-php-ext-install sockets

ADD crontab /etc/cron.d/php-cron
RUN chmod 0644 /etc/cron.d/php-cron
RUN touch /var/log/cron.log
RUN /etc/init.d/cron start

RUN echo 'Done Setting Up....'
# CMD ["/usr/bin/tail -f /var/log/cron.log"]
