FROM ubuntu 

RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    && pip3 install --upgrade pip

    # Install Python packages
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create a directory inside the container 
RUN mkdir -p /home/doc-bd-a1

# Copy dataset to the container 
COPY creditcard.csv /home/doc-bd-a1/

# Copy the application files into the container
COPY . /app

# Specify the command to run your application
CMD ["/bin/bash"]

