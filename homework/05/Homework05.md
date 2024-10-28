**Question 1**
   - Install Pipenv
   - What's the version of pipenv you installed?
   - Use --version to find out

   **Answer**

      - pip install pipenv
      - pipenv --version

      > pipenv version 2024.2.0





**Question 2**
   - Use Pipenv to install Scikit-Learn version 1.5.2
   - What's the first hash for scikit-learn you get in Pipfile.lock?

   **Answer**

    - cd ml-zoomcamp-2024/homework/
    - mkdir 05
    - cd 05
    - pipenv --python 3.11.5
    - pipenv install scikit-learn==1.5.2

    *First hash for scikit-learn in the Pipfile.lock is*

     > "sha256:03b6158efa3faaf1feea3faa884c840ebd61b6484167c711548fce208ea09445"





**Question 3**

  - Let's use these models!
    - Write a script for loading these models with pickle
    - Score this client:

         > {"job": "management", "duration": 400, "poutcome": "success"}

    *What's the probability that this client will get a subscription?*

    - 0.359
    - 0.559
    - 0.759
    - 0.959

  **Answer**

   *First downloading the DictVetorizer and Logistic Regression model by*

    > PREFIX=https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/cohorts/2024/05-deployment/homework

    > wget $PREFIX/model1.bin

    > wget $PREFIX/dv.bin

   *Script named 'question3.py' load these models with pickle and scores the given customer/client*

      > python question3.py

       *Yeilds output*
        > Subscription Probability: 0.759
        > Subscription Decision: True

    > *So it is seen that the script when run gives us that this client will get a subscription with **0.759** probability*




**Question 4**

  *Now let's serve this model as a web service*

    - Install Flask and gunicorn (or waitress, if you're on Windows)
    - Write Flask code for serving the model
    - Now score this client using requests:

      > url = "YOUR_URL"
        client = {"job": "student", "duration": 280, "poutcome": "failure"}
        requests.post(url, json=client).json()

  *What's the probability that this client will get a subscription?*

    - 0.335
    - 0.535
    - 0.735
    - 0.935

  
  **Answer**

  *Changed to target directory*

   > cd ml-zoomcamp-2024/homework/05

  *Entering target virtual environment*

   > pipenv shell

  *Inside the virtual environment changed to target directory*

   > (05) sidd4ml@LAPTOP-37937H2A:~$ cd ml-zoomcamp-2024/homework/05

  *Installing flask, request and gunicorn inside the environment*

   > pipenv install flask gunicorn

   > pipenv istall requests

  
  *The script named question4.py serves the model as a web service and the script subs-prob-testQ4.py invokes it to get the subscription probability*

   > *Now we need to run the gunicorn WSGI http server to make the web-service active for consumption/use by running this command inside the environment*

     > gunicorn --bind 0.0.0.0:9696 question4:app

   > *Then invoke web-service through the subs-prob-test.py (can be invoked from both the virtaul and global environment)*

     >05sidd4ml@LAPTOP-37937H2A:~/ml-zoomcamp-2024/homework/05$ python subs-prob-testQ4.py
      The client may not subscribe to a term deposit. Low probability value of 0.335

   > *So the output 'The client may not subscribe to a term deposit. Low probability value of 0.335' gives us value of **0.335** for the probability*




**Question 5**

   - Download the base image svizor/zoomcamp-model:3.11.5-slim. You can easily make it by using docker pull command.

   - So what's the size of this base image?

     > 45 MB

     > 130 MB

     > 245 MB

     > 330 MB

    *You can get this information when running docker images - it'll be in the "SIZE" column*


**Answer**

 *As instructed, issued the docker pull commmand (from inside the virtual environment)*

  > docker pull svizor/zoomcamp-model:3.11.5-slim

 *which pulled the image successfully*

 *Thereafter, checking the size of the image under docker images*
  
   >(05) sidd4ml@LAPTOP-37937H2A:~/ml-zoomcamp-2024/homework/05$ docker images

    REPOSITORY              TAG           IMAGE ID       CREATED        SIZE
    zoomcamp-test           latest        2bb522da07a8   15 hours ago   801MB
    svizor/zoomcamp-model   3.11.5-slim   975e7bdca086   9 days ago     130MB

 *This shows the base image is **130 MB** in  size*



**Question 6**

 - Let's run your docker container!

 - After running it, score this client once again:

       url = "YOUR_URL"

       client = {"job": "management", "duration": 400, "poutcome": "success"}
      
       requests.post(url, json=client).json()

 *What's the probability that this client will get a subscription now?*

       0.287
       0.530
       0.757
       0.960


**Answer**


  *First the Dockerfile was created with appropriate entries/inputs*


  *Thereafter we build the docker image as follows:*

   > docker build -t siddg/zoomcamp-model .


  *We check if the image was successfuly built:*

   >  (05) sidd4ml@LAPTOP-37937H2A:~/ml-zoomcamp-2024/homework/05$ docker images

      REPOSITORY              TAG           IMAGE ID       CREATED         SIZE
      siddg/zoomcamp-model    latest        a66f8193c2df   8 minutes ago   549MB
      zoomcamp-test           latest        2bb522da07a8   16 hours ago    801MB
      svizor/zoomcamp-model   3.11.5-slim   975e7bdca086   9 days ago      130MB


  *Now we create need to create one more script to test the new customer's subscription probability. We name it subs-prob-testQ6.py*


  *Subsequently, we run the docker image we built:*

  > (05) sidd4ml@LAPTOP-37937H2A:~/ml-zoomcamp-2024/homework/05$ docker run -it --rm -p 9696:9696 siddg/zoomcamp-model

    [2024-10-28 11:38:15 +0000] [1] [INFO] Starting gunicorn 23.0.0
    [2024-10-28 11:38:15 +0000] [1] [INFO] Listening at: http://0.0.0.0:9696 (1)
    [2024-10-28 11:38:15 +0000] [1] [INFO] Using worker: sync
    [2024-10-28 11:38:15 +0000] [7] [INFO] Booting worker with pid: 7  


  *Finally we run the subs-prob-testQ6.py script for evaluating the given client's subscription probability from the model served by the webservice deployed in the docker container*

    > 05sidd4ml@LAPTOP-37937H2A:~/ml-zoomcamp-2024/homework/05$ python subs-prob-testQ6.py
      The client may subscribe to a term deposit. High probability value of 0.759

  *Hence we can see that the nearest value in the options to 0.759 is 0.757 and so we conclude the probability is **0.757** that this client will get a subscription.*