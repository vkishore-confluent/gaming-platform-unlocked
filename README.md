# Gaming Platform Unlocked - Data Streaming Pipeline for Gaming Applications

In this demonstration, we present three essential use cases that illustrate the versatility and reliability of Confluent Cloud for building your data streaming pipeline for your gaming applications. 

These use cases provide valuable insights into the technical requirements and considerations for creating a robust and efficient gaming data streaming system. By exploring these scenarios, you will gain a deeper understanding of how our platform can be adapted to various real-world applications.

# Requirements

In order to successfully complete this demo you need to install few tools before getting started.

- If you don't have a Confluent Cloud account, sign up for a free trial [here](https://www.confluent.io/confluent-cloud/tryfree).
- Install Confluent Cloud CLI by following the instructions [here](https://docs.confluent.io/confluent-cli/current/install.html).
- Please follow the instructions to install Terraform if it is not already installed on your system [here](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)  
- Install Python on your local system by following the instructions [here](https://realpython.com/installing-python).
   > **Note:** This demo uses Python 3.11.3 version
- This demo uses python modules. You can install this module through `pip` or `pip3`.

  ```
  pip3 install <module-name>
  ```

## Prerequisites

### Confluent Cloud

1. Sign up for a Confluent Cloud account [here](https://www.confluent.io/get-started/).
2. After verifying your email address, access Confluent Cloud sign-in by navigating [here](https://confluent.cloud).
3. When provided with the _username_ and _password_ prompts, fill in your credentials.

   > **Note:** If you're logging in for the first time you will see a wizard that will walk you through the some tutorials. Minimize this as you will walk through these steps in this guide.

4. Create Confluent Cloud API keys by following the steps in UI. Click on the hamburger icon that is present on the right top section and click on Cloud API Key.

<div align="center"> 
  <img src="images/cloud1.jpeg" width =100% heigth=100%>
</div>

Now Click Add Key to generate API keys and store it as we will be using that key in this demo.

 <div align="center"> 
  <img src="images/cloud2.jpeg" width =100% heigth=100%>
</div>
    
   > **Note:** This is different than Kafka cluster API keys.

## Setup

1. This demo uses Terraform  to spin up resources that are needed.

2. Update the `terraform/variables.tf` file for the following variables with your Cloud API credentials.

```
variable "confluent_cloud_api_key" {
  default = bash "Replace with your API Key created during pre-requsite"   
}

variable "confluent_cloud_api_secret" {
  default = bash "Replace with your API Secret created during pre-requsite"   
}
```

 ### Build your cloud infrastructure

1. Navigate to the repo's terraform directory.
   ```bash
   cd terraform
   ```

1. Initialize Terraform within the directory.
   ```
   terraform init
   ```

1. Apply the plan to create the infrastructure.

   ```
   terraform apply 
   ```

   > **Note:** Read the `main.tf` configuration file [to see what will be created](./terraform/main.tf).

## Architectural Diagrams:

### Multiple Event Types in Single Topic:

sample text here:

<div align="center"> 
  <img src="images/gaming_platform_unlocked_1.png" width =100% heigth=100%>
</div>

### Preventing duplicate message with ksqlDB:

sample text here:

<div align="center"> 
  <img src="images/gaming_platform_unlocked_2.png" width =100% heigth=100%>
</div>

### Observability of the gaming platform:

sample text here:

<div align="center"> 
  <img src="images/gaming_platform_unlocked_3.png" width =100% heigth=100%>
</div>
