FROM ubuntu:16.04
# Update packages
RUN apt-get update -y


# Install Python Setuptools
RUN apt-get install -y python-setuptools
RUN apt-get install -y build-essential libssl-dev libffi-dev libevent-dev
RUN apt-get install -y python-dev
RUN apt-get install -y python-tk

# apt-get and system utilities
RUN apt-get -qq -y install curl
RUN apt-get update && apt-get install -y \
    curl apt-utils apt-transport-https debconf-utils gcc build-essential g++-5\
    && rm -rf /var/lib/apt/lists/*

# adding custom MS repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# install SQL Server drivers
RUN apt-get update && ACCEPT_EULA=Y apt-get -y install msodbcsql
RUN apt-get -y install unixodbc unixodbc-dev freetds-dev freetds-bin tdsodbc

#docker tds addition
#ADD etc_freetds_freetds.conf /etc/freetds/freetds.conf
#ADD etc_odbc.ini /etc/odbc.ini
ADD etc_odbcinst.ini /etc/odbcinst.ini

# install SQL Server tools
RUN apt-get update && ACCEPT_EULA=Y apt-get -y install mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"

# Install pip
RUN easy_install pip

# Add and install Python modules
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt

# Bundle app source
ADD . /src

# Expose
EXPOSE  5000

# Run
CMD ["python", "/src/application.py"]
