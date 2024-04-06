#!/bin/bash

# Define the number of workers to be used by the API
CPU_CORES=$(nproc --all)
WORKERS_NUM=$((CPU_CORES + 1))
HOST=0.0.0.0
PORT=8000

# Check if conda is installed
if command -v conda &> /dev/null; then
    echo "Conda is installed."
else
    # Download and install conda
    echo "Conda is not installed. Download and instalation in progress..."
    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm -rf ~/miniconda3/miniconda.sh
    eval "$(~/miniconda3/bin/conda shell.bash hook)"
    conda init
    export PATH=$PATH:~/miniconda3/bin/
fi

# Check if conda environment exists
ENV_NAME="restapi"
if conda env list | grep -q "\<$ENV_NAME\>"; then
    # Activate the conda environment if already exists
    echo "Conda environment '$ENV_NAME' exists, activating..."
    eval "$(~/miniconda3/bin/conda shell.bash hook)"
    conda init
    conda activate $ENV_NAME
else
    # Create a new conda environment and install the required packages if it does not exist
    echo "Conda environment '$ENV_NAME' does not exist, creating..."
    conda create -n $ENV_NAME python=3.12.2
    conda activate $ENV_NAME
    pip install -r requirements.txt
fi

# Run the API, let the user choose between custom or pydantic validations
echo ""
read -p "Run API with custom or pydantic validations? (custom/pydantic): " checks
if [ "$checks" == "custom" ]; then
    # Run the API with custom validations
    echo "Running API with manual validations..."
    echo "Running API tests..."
    pytest --verbose --pyargs src
    echo "Starting the API service with '$WORKERS_NUM' workers..."
    uvicorn src.app_custom_validations:app --workers $WORKERS_NUM --host $HOST --port $PORT
else
    # Run the API with pydantic validations
    echo "Running API with pydantic validations..."
    echo "Starting the API service with '$WORKERS_NUM' workers..."
    uvicorn src.app_pydantic_validations:app --workers $WORKERS_NUM --host $HOST --port $PORT
fi

