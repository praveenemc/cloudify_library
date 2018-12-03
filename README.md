# cloudify_library
This library uses the cloudify client to test some of the functions of cloudify manager (version 4.3.1)
This has been tested in Ubuntu 14.04 platform using python virtualenv 16.1.0

Please follow the below steps to test the library:

## Step1:

Install the virtual env, git, vim:
```
$sudo apt-get install python-virtualenv git vim -y
```

## Step2:
Create venv to test the cloudifyclient functionality:
```
$virtualenv cloudifyclient_venv
```

## Step3:
Activate the venv:
```
$source cloudifyclient_venv/bin/activate
$cd cloudifyclient_venv
```

## Step4:
Install the required python packages:
```
$pip install pip==9.0.1
$pip install prettytable
$pip install cloudify
$sudo pip install cloudify_rest_client
```
This installed cloudify-rest-client verion is 4.3.3. The list of all installed packages can be found [here](/pip_installed_packages.JPG)

## Step5:
Clone this cloudify_library repo
```
$git clone https://github.com/praveenemc/cloudify_library.git
$cd cloudify_library
```

## Step6:
Update the cloudify manager details in the **config.py** file.
Run the test code as below:
```
$python test_cfy_library.py > output_dec4.txt
```

The output file output_dec4.txt is shared here for reference and also the test_blueprint_uploaded_GUI_Dec4.JPG GUI screenshot. 
