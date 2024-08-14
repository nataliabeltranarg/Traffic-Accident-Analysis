# Analysis of Accidents in the US Dataset
## Final Project for Computing for Data Science

Authors: 
* Maëlys Boudier
* Natalia Beltran
* Miguel Handt Fueyo

### Data: 
**Source**: https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents/data

### General Overview of Library
The Repository Architecture is detailed in its entirety at the bottom of this README.md file. The data library contains a dataanalysis package consisting of 5 subfolders 
* **Load**: any functions pertaining to data loading and splitting of data
* **Preprocessing**: any functions conducting preliminary processing and data cleaning
* **Features**: any function transforming/creating new features through feature engineering
* **Model**: any functions creating and tuning a model
* **Metrics** any functions evaluating model performance

To ensure that each function is readable and usable, they all have a corresponding docstring which follows the format below. This allows teammates and new members to easily check what a function does and what the arguments and outputs consist of.  

**Docstring Format:**

    """ 
    explain what function does

    Args:
        name_variable (type) : what this variable corresponds to
        other_variable (type) : what this variable corresponds to

    Returns:
        type of output
    """

### Library Modules
#### Load
The **load** folder contains modules pertaining to loading data and splitting data into training and testing frames. 

#### Preprocessing
The **preprocessing** folder contains modules to conduct preliminary processing of the data such as treating missing values (the python file contains multiple techniques each implemented as a function), treat outliers, convert data to timedate format, and standardize. 

#### Features
The **features** folder contains modules to conduct feature engineering reorganized by types of data the feature engineering impacts: categorical features (binning, one-hot encoding, and binary encoding), heat features (temperature conversions, calculation of a heat index), road features (summing of road feature booleans), state features (grouping states into regions in the US), and time features (extracting month and calculating time difference). 

#### Model
The **model** folder contains a module to create a model class and run a model (as of now, only a Random Forest Classifier has been developped). The class also has a method to conduct hyperparameter tuning. 

#### Metrics
The **metrics** folder contains a model to create a metrics class and get the f1 score for given predictions and target values as well as a confusion matrix. 

### Scaling the Library

When developping a new function to scale the library, the team member must include a docstring explaining the goal of the function, the arguments (type and definition) and the outputs (type and definition). 

If a team member wants to add a new function, they must first decide in which subfolder to add it based on the utility of the function (check **Library Modules** section for clearer definitions). After, they must either create a new module by creating a .py file for the function or add it to a relevant module. Then, they must ensure that the requirements.txt file has been updated with necessary packages (if any) and reinstall the new version of the library (steps detailed in **Install Library** section). Then, the team member may add it to the pipeline in income_analysis.ipynb jupyter notebook if they wish to run it in the data analysis. 

It is also advisable to add tests to the test folder to ensure that that these will run in the future even if other changes are made. The team member must run all the tests to check that there are no issues caused by this new or modified function to any other functions (steps detailed in **Run Tests** section). 

### Install Library
* Step 1: open terminal and run following commands
* Step 2: conda activate *(insert env here)*
* Step 3: cd *(insert library file path here)*
* Step 4: pip install wheel
* Step 5: python setup.py sdist bdist_wheel
* Step 6: pip install .

### Run Tests
The test folder carries out tests for the preprocessing and feature modules which can be run using pytest. The command to run the tests are:
* Step 1: open terminal and run following commands
* Step 2: conda activate *(insert env here)*
* Step 3: cd *(insert test file path here)*
* Step 4: pytest test
    * run only 1 test file: pytest test_name_of_test.py  
* Step 5: pytest --cov

Note: Implement step 4 to run tests and step 5 to run test coverage

### Repository Architecture
```bash 
computing-finalproj
├── datalibrary
│   ├── dataanalysis
│   │   ├── __init__.py
│   │   ├── features
│   │   │   ├── __init__.py
│   │   │   ├── categoricalfeatures.py
│   │   │   ├── heatfeatures.py
│   │   │   ├── roadfeatures.py
│   │   │   ├── statefeatures.py
│   │   │   └── timefeatures.py
│   │   ├── load.py
│   │   │   ├── __init__.py
│   │   │   ├── loading.py
│   │   │   └── splitting.py
│   │   ├── model.py
│   │   │   ├── __init__.py
│   │   │   └── rfmodel.py
│   │   ├── metrics.py
│   │   │   ├── __init__.py
│   │   │   └── metrics.py
│   │   └── preprocessing.py
│   │       ├── __init__.py
│   │       ├── missingvalues.py
│   │       ├── outliertreatment.py
│   │       ├── standardization.py
│   │       └── timedata.py
│   ├── LICENSE
│   ├── requirements.txt
│   └── setup.py
├── test
│   ├── test_features
│   │   ├── test_categoricalfeatures.py
│   │   ├── test_heatfeatures.py
│   │   ├── test_roadfeatures.py
│   │   ├── test_statefeatures.py
│   │   └── test_timefeatures.py
│   └── test_preprocessing.py
│       ├── test_missingvalues.py
│       ├── test_outliertreatment.py
│       ├── test_standardization.py
│       └── test_timedata.py
├── accident_analysis.ipynb
├── US_Accidents_March23_sample.csv
├── US_Accidents_Analysis_Presentation.pdf
└── README.md
```
