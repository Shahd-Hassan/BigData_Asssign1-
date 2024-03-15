#!/bin/bash

# Set the container name
CONTAINER_NAME="priceless_beaver"

# Directory on the container where the output files are located
CONTAINER_OUTPUT_DIR="/home/doc-bd-a1/"

# Local directory path where you want to copy the output files
LOCAL_OUTPUT_DIR="C:\Users\shahd's Laptop\bd-a1\service-result"

# Print debugging information
echo "Copying files from container name: $CONTAINER_NAME"
echo "Container output directory: $CONTAINER_OUTPUT_DIR"
echo "Local output directory: $LOCAL_OUTPUT_DIR"

# Copy output files from the container to the local machine
docker cp $CONTAINER_NAME:$CONTAINER_OUTPUT_DIR/res_dpre.csv "$LOCAL_OUTPUT_DIR"
docker cp $CONTAINER_NAME:$CONTAINER_OUTPUT_DIR/eda-insight-1.txt "$LOCAL_OUTPUT_DIR"
docker cp $CONTAINER_NAME:$CONTAINER_OUTPUT_DIR/eda-insight-2.txt "$LOCAL_OUTPUT_DIR"
docker cp $CONTAINER_NAME:$CONTAINER_OUTPUT_DIR/eda-insight-3.txt "$LOCAL_OUTPUT_DIR"
docker cp $CONTAINER_NAME:$CONTAINER_OUTPUT_DIR/k.txt "$LOCAL_OUTPUT_DIR"
docker cp $CONTAINER_NAME:$CONTAINER_OUTPUT_DIR/vis.png "$LOCAL_OUTPUT_DIR"


# Print message indicating completion of file copying
echo "Files copied successfully to $LOCAL_OUTPUT_DIR"

# Stop the container
docker stop $CONTAINER_NAME
