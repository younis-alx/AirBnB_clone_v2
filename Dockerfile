FROM ubuntu:20.04

# Install Python, pip, and other necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Install MySQL 8.0
RUN apt-get update && \
    DEBIAN_FRONTEND="noninteractive" apt-get install -y mysql-server-8.0 && \
    apt-get clean

# Set up MySQL configuration
RUN service mysql start && \
    mysql -u root -e "ALTER USER 'root'@'localhost' IDENTIFIED BY 'asd';"

# Upgrade pip
RUN pip3 install --upgrade pip

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy your application code to the Docker image
COPY . /AIRBNB_clone_v2

# Set the working directory
WORKDIR /AIRBNB_clone_v2

# Expose the MySQL port
EXPOSE 3306

# Specify the command to run your application
CMD [ "python3", "console.py" ]