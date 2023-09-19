FROM ubuntu:20.04.3

# Set up Environment variables
ENV HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db

# Install Python and other necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip mysql-server-8.0 && \
    apt-get clean

# Upgrade pip
RUN pip3 install --upgrade pip

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Set up MySQL configuration
RUN mysql -u root -e "ALTER USER 'root'@'localhost' IDENTIFIED BY 'asd';"

# Copy your application code to the Docker image
COPY . /AIRBNB_clone_v2

# Set the working directory
WORKDIR /AIRBNB_clone_v2

# Specify the command to run your application
CMD [ "python3", "/AIRBNB_clone_v2/console.py" ]