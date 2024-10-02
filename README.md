# IR-Project
Information Retrieval Project
## Table of Contents

- [Prerequisites](#prerequisites)
- [Setting Up the Environment](#setting-up-the-environment)
  - [Option 1: Using Conda](#option-1-using-conda)
  - [Option 2: Using Pip](#option-2-using-pip)
- [Running the Project](#running-the-project)
- [Additional Notes](#additional-notes)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Ensure you have the following installed on your system:

- [Git](https://git-scm.com/downloads)
- [Anaconda](https://www.anaconda.com/products/distribution) (if using `conda`)
- [Python](https://www.python.org/downloads/) (if using `pip`)

## Setting Up the Environment

This project requires specific dependencies that can be installed using either `conda` or `pip`. Follow the instructions for the package manager you prefer.

### Option 1: Using Conda

1. **Clone the Repository**:
   Open your Anaconda Prompt or command prompt and run:
   ```bash
   git clone https://github.com/leloso/IR-Project.git
   cd repo-name
   conda env create -f environment.yml
   conda activate myenv
   conda list #έλεγχχος αν έχουν γίνει όλα καλά bash```
   
   Updating the Environment (if needed): If there are updates to the environment.yml file or if you add new dependencies later, you can update the environment with:
Το layout του working directory θα πρέπει να έχει την γενική μορφή:
IRProject/
|--src/
     |--main.py
     |--utils.py
     ....... etc
|--data/
     |--dataset.csv
|--README.md

etc ......

Για το setup του python environment αφού γίνει clone το repo στο working directory
