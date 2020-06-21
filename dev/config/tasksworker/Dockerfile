FROM php:7.2-fpm
ADD gearman-manager.ini /etc/gearman-manager.ini
ADD tasksworker.py /usr/local/bin/tasksworker.py
ADD process-sms-queue.sh /process-sms-queue.sh
ADD clean-instances.sh /clean-instances.sh
ADD hourly-scripts.sh /hourly-scripts.sh
ADD daily-scripts.sh /daily-scripts.sh

RUN chmod 0755 /process-sms-queue.sh
RUN chmod 0755 /clean-instances.sh
RUN chmod 0755 /hourly-scripts.sh
RUN chmod 0755 /daily-scripts.sh
ADD tasksworker.service /etc/systemd/system/tasksworker.service
ADD restart-tasksworker.sh /usr/local/bin/restart-tasksworker.sh
ADD tasksworker-startup.sh /tasksworker-startup.sh
RUN mkdir /var/escweb; mkdir /var/escweb/media; mkdir /var/escweb/uploads; mkdir /var/escweb/log; mkdir /var/escweb/cache; mkdir /var/escweb/templates;
RUN touch /var/escweb/log/error.log
RUN chmod -R 777 /var/escweb/*
RUN apt-get update && apt-get install -y \
        python2.7 \
        python-pip \
        gearman \
        cron \
        python-setproctitle \
        imagemagick \
        libmagickwand-dev \
        nano \
        zlib1g-dev \
        libzip-dev \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install mysqli \
    && docker-php-ext-install bcmath \
    && docker-php-ext-install zip \
    && pecl install redis-4.0.1 \
    && pecl install apcu-5.1.11 \
    && pecl install imagick-3.4.3 \
    && docker-php-ext-enable imagick \
    && docker-php-ext-enable redis \
    && docker-php-ext-enable apcu \
    && docker-php-ext-install pcntl \
    && docker-php-ext-install sockets

RUN echo 'Done Setting Up....'
CMD ["/tasksworker-startup.sh"]
