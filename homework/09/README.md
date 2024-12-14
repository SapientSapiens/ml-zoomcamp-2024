## For Question 1 to Question 4 please check Homework09.ipynb ##


## For Question 5 ##

*Testing this file locally with ipython after converting the notebook to script and doing required changes for lambda deployement and invoking the function from this file.*

![alt text](images/image.png)

*Pulled the Docker image*

![alt text](images/image-1.png)

**So we can see that the size of the base image is 782MB**

## For Question 6 ##

*Created the Dockerfile*

![alt text](images/my_Dockerfile_snapshot.jpg)

*And built the image*

![alt text](images/creating_docker_image.jpg)

*Built Docker image showing on list*

![alt text](images/image-5.png)

*Created a test.py script for testing the model within the image to be run inside Docker*

![alt text](images/image-4.png)

*Ran the Docker image and executed the test.py*

![alt text](images/test_script_run.jpg)

**So we can see that the output of the model is 0.429**



## Publishing it to AWS ##

 ### Publishing the image to ECR ###

 - ### Install awscli ###

 ![alt text](images/install-awscli.jpg)

 - ### Create AWS Elastic Container Registry repository and log in to the same. You may have to configure with ```aws configure``` prior to this, if not done already. ###

 ![alt text](<images/create ECR repo and login to that.jpg>)

 - ### AWS ECR repository created ###

 ![alt text](images/aws-repo-screenshot.jpg)

 - ### Set the variables for REMOTE_URI to the ECR ###

 ![alt text](images/REMOTE_URI_SET.jpg)

 - ### Tag the Docker image built on the local machine and push it to the ECR ###

 ![alt text](images/REMOTE_URI_SET_TAGGING_PUSH.jpg)

 - ### The image would be pushed to the ECR repository ### 
 
 ![alt text](<images/TAGGING IMAGE AND PUSHING TO ECR.jpg>)

 - ### Pushed image showing in the ECR at AWS ###

 ![alt text](<images/Image pushed to ECR.jpg>)



 ### Creating a lambda function in AWS, using the ECR image ###
 
 - ### Create the AWS Lambda function choosing options as below ###

 ![alt text](<images/finally create the lambda function.jpg>)

 - ### Select the required container image from the ECR repository ### 

 ![alt text](<images/select container image from ECR.jpg>)

 - ### You should get the lambda function created shown as below ###

 ![alt text](<images/successfully created lambda function.jpg>)



 ### Give it more RAM and increase the timeout and Test it ###

 - ### Edit basic settings to increase Memory to 1024 MB and timeout to 30 seconds ###

 ![alt text](<images/Increased RAM and time out duration.jpg>)

 - ### Finally testing the lammbda function by creating & saving a Test Event and testing it ###

 ![alt text](<images/lambda function test and result.jpg>)


 ### Expose the lambda function using API Gateway ###

 - ### Pull up AWS API Gateway section and first create a new REST API ###

 ![alt text](<images/Creating REST API.jpg>)
 
 - ### Now create a Resource for the created API ###

 ![alt text](<images/creating resource for API.jpg>)

 - ### Then choose a API action (POST in our case) for the created Resource ###

 ![alt text](<images/creating method for created resource.jpg>)

 - ### Subsequently, create a Method for the Resource ###

 ![alt text](<images/creating method for created resources.jpg>)

 - ### After Method is created, you shall get this. You can test the Method from here. ###

 ![alt text](<images/API Gateway (method created for resourse ).jpg>)

 - ### Now you can Deploy the API by creating a Stage ###

 ![alt text](<images/deploying the API.jpg>)

 - ### We can see the stage ('test' in our case) has been created and the URL for public access of the API is generated here. ###

 ![alt text](<images/api gateway stage created with public url.jpg>)



 ### Testing the Lamda function with the API ###

 - ### A test script aws_test.py is created for testing the Lambda Function through the API from the gateway ###

 ![alt text](<images/final test script to test the lambda function through API gateway.jpg>)

 - ### As we can see from the above image, the test script executes successfully, calling the lambda function through tthe API ###



