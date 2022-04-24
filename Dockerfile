FROM debian:buster 

# Updaten und Apache und Python installieren
RUN apt update
RUN apt -y install apache2 apache2-utils python3 && apt-get clean

# CGI einrichten
RUN a2enmod cgi
COPY conf/cgi-apache.conf /etc/apache2/conf-available/cgi-enabled.conf
RUN a2enconf cgi-enabled

# Kopieren von Source Code
RUN mkdir -p /var/www/html/cgi
ADD src /var/www/html/cgi
RUN chmod 705 /var/www/html/cgi/index.cgi
RUN chmod 666 /var/www/html/cgi/todo_cgi.log
RUN chmod 666 /var/www/html/cgi/todo.db

# Apache Scheiß
ENV APACHE_RUN_DIR /var/lib/apache/runtime
ENV APACHE_PID_FILE /var/run/apache2/apache2
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
RUN mkdir -p ${APACHE_RUN_DIR}
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Apache neu starten
RUN service apache2 restart

# Apache als Dienst für Docker
ENTRYPOINT ["/usr/sbin/apache2"]
CMD ["-D", "FOREGROUND"]