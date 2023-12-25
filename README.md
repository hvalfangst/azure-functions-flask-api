# Azure Function in Python with CI/CD 

Azure Function programmed in Python with the Flask HTTP framework, 
providing endpoints for encryption utilizing AES 256 CBC algorithm. 
A CI/CD pipeline has been implemented with GitHub Actions. 
It will build, package and deploy this application to Azure Function Apps
on any repository pushes. Azure resources are provisioned with Terraform.

## Requirements

* x86-64
* Linux/Unix
* [Python](https://www.python.org/downloads/)

## Creating resources

The shell script 'up' allocates Azure resources with Terraform.

## Deleting resources

The shell script 'down' deallocates Azure resources.


## Guide

### 1. Provision Azure Resources

- Run the 'up' script to provision Azure resources.

### 2. Access Azure Portal

- Open your browser and navigate to the Azure Portal.

### 3. Configure Deployment Credentials

- Navigate to your newly created Function App 'hvalfangstfunctionapp'.
- Click on 'Deployment Center' under 'Settings'.
- Choose GitHub as the source and proceed to authenticate & authorize your GH account.
- After your account has been validated you may now choose a target repository and branch.
- Click 'Save'.
- A new folder named '.github' will now be pushed to your repository on behalf of Azure.
- This folder contains the GitHub Action Workflow definition, which enables CI/CD.