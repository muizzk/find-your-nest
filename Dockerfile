FROM debian:10


RUN apt-get update



RUN apt-get install -y apache2 \
    && apt-get install -y php-mysql \
    &&  apt-get install -y libapache2-mod-php wget w3m

#Télécharger le zip de dokuwiki
#Dézipper
#Mettre le dossier dans /var/www/html
RUN wget -O /usr/src/wordpress.tar.gz https://wordpress.org/wordpress-5.2.2.tar.gz 

RUN cd /usr/src/ \     
    && tar xzvf wordpress.tar.gz \
    && rm -fr /var/www/html \
    && mv wordpress /var/www/html

RUN chown -R www-data:www-data /var/www/html

EXPOSE 80 

CMD /etc/init.d/apache2 start \
    && while true ; do sleep 1; done

 
 


