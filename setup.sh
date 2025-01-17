#!/bin/bash

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Node.js is not installed. Installing Node.js..."
    # Install Node.js (includes npm)
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get install -y nodejs
else
    echo "Node.js is already installed. Version: $(node -v)"
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "npm is not installed. Installing npm..."
    sudo apt-get install -y npm
else
    echo "npm is already installed. Version: $(npm -v)"
fi

# Check if @apidevtools/swagger-parser is installed
if ! npm list -g @apidevtools/swagger-parser &> /dev/null; then
    echo "@apidevtools/swagger-parser is not installed. Installing..."
    npm install -g @apidevtools/swagger-parser
else
    echo "@apidevtools/swagger-parser is already installed."
fi

echo "Setup completed successfully!"
