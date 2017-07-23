# eb-docker-flask-mssql
A Flask Application template that uses MS-SQL, containerized for docker, for deployment in Elastic Beanstalk.

### Instructions 
1. Setup Docker in your local. Install Docker, Docker Compose
2. Clone this directory to your local
3. Navigate to the master eb-docker-flask-mssql directory and execute `docker-compose up`
4. navigate to the local home page using the docker http://192.168.99.100:5000  (or whichever docker chooses as its home IP)

### Instructions (Windows)
1. Install Docker Toolbox for Windows - https://docs.docker.com/toolbox/toolbox_install_windows/
2. Clone this directory to your local
3. Navigate to the eb-docker-flask-mssql directory using Docker Quickstart terminal
4. Execute `docker-compose up`
5. Navigate to the local home page using the docker http://192.168.99.100:5000  (or whichever docker chooses as its home IP)

### Instructions (AWS - Elastic Beanstalk Deployment)
1. Create a new environment, Choose the "Generic Docker" Platform, with t2.small as the minimum server size 
2. Navigate to the `ElasticBeanstalk-Docker-Flask-Template` Folder, then place the contents of that folder into a zip file
3. deploy the zip file into the AWS environment.
