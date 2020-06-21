FROM nginx:1.15.0
ADD sites-enabled /sites-enabled/
RUN rm -rf /etc/nginx/sites-enabled
RUN ln -s /sites-enabled /etc/nginx/sites-enabled
ADD nginx.conf /etc/nginx/nginx.conf
ADD create_s3_buckets.py /create_s3_buckets.py
# ADD init-hhvm.sh /init-hhvm.sh
# RUN chmod 755 /init-hhvm.sh
# RUN python /create_s3_buckets.py

RUN export LANG=en_US.UTF-8

#RUN apt-get update
#RUN apt-get install -y \
#    apt-transport-https \
#    software-properties-common \
#    curl \
#    gnupg2 \
#    nano \
#    dbus-user-session \
#    sudo


#RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xB4112585D386EB94
#
#RUN add-apt-repository https://dl.hhvm.com/debian
#RUN apt-get update
#RUN apt-get install -y hhvm