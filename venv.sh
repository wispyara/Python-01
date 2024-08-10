#!/bin/bash
set -e

# 1. Remove any existing virtual environment directory
rm -rf myenv

# 2. Display the default python executable path
printf "Default python executable\n"
which python

# 3. Create a new virtual environment named 'myenv'
printf "\nLet's create the venv\n"
python -m venv myenv
sleep 5

# 4. Activate the virtual environment (Windows-specific)
source myenv/Scripts/activate

# 5. Install dependencies from the existing requirements.txt
if [ -f "requirements.txt" ]; then
    printf "\nInstalling dependencies from existing requirements.txt\n"
    pip install -r requirements.txt
else
    printf "\nrequirements.txt not found. Exiting.\n"
    exit 1
fi

# 6. Create a new requirements.txt file that lists all the installed packages
printf "\nCreating updated requirements.txt\n"
pip freeze > requirements.txt