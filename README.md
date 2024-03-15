# Big Data Assignment 1

Welcome to the Big Data Assignment 1 project! This project aims to demonstrate various data preprocessing techniques on the Credit Card Fraud Detection dataset.
#######################################################################################################################

Contributors:
--------------
1- Shahd Hassan --> 211001636 [1B]
2- Kenzy Khaled --> 211001724 [1A]
3- Cecilia Mohamed --> 211002069 [1A]
4- Mohamed Khaled --> 211001722 [1A] 
_____________________________________________________
* Docker Commands Used:
------------------------
C:\Users\shahd's Laptop>mkdir bd-a1
C:\Users\shahd's Laptop>cd bd-a1
C:\Users\shahd's Laptop\bd-a1>

C:\Users\shahd's Laptop\bd-a1>bash open 
C:\Users\shahd's Laptop>start docker

C:\Users\shahd's Laptop>cd bd-a1

C:\Users\shahd's Laptop\bd-a1>docker build -it bd-a1. 
C:\Users\shahd's Laptop\bd-a1>docker run -it  bd-a1. 

root@748e3ab26c2c:/# cd home/doc-bd-a1/
root@748e3ab26c2c:/home/doc-bd-a1# nano load.py
root@748e3ab26c2c:/home/doc-bd-a1# nano dpre.py
root@748e3ab26c2c:/home/doc-bd-a1# nano eda.py
root@748e3ab26c2c:/home/doc-bd-a1# nano vis.py
root@748e3ab26c2c:/home/doc-bd-a1# nano model.py
root@748e3ab26c2c:/home/doc-bd-a1# python3 load.py creditcard.csv
Dataset loaded successfully.

root@748e3ab26c2c:/home/doc-bd-a1# exit
exit


C:\Users\shahd's Laptop\bd-a1>pip install nano
Defaulting to user installation because normal site-packages is not writeable
Collecting nano
  Downloading nano-0.10.0-py2.py3-none-any.whl (68 kB)
     ---------------------------------------- 68.1/68.1 kB 371.1 kB/s eta 0:00:00
Installing collected packages: nano
Successfully installed nano-0.10.0

[notice] A new release of pip is available: 23.0.1 -> 24.0
[notice] To update, run: python.exe -m pip install --upgrade pip





C:\Users\shahd's Laptop\bd-a1>.\final.sh

C:\Users\shahd's Laptop\bd-a1>.\files.sh


C:\Users\shahd's Laptop\bd-a1>docker tag bd-a1 shahdhassan9903/bd-a1:latest

C:\Users\shahd's Laptop\bd-a1>docker login
Authenticating with existing credentials...
Login Succeeded

C:\Users\shahd's Laptop\bd-a1>docker push shahdhassan9903/bd-a1:latest

273748eb0e4e: Pushing [============>                                      ]  37.29MB/150.8MB
2ab1d3d1d326: Pushing [===========>                                       ]  35.62MB/150.8MB
Authenticating with existing credentials...
550ee465949f: Pushing [=>                                                 ]  15.02MB/513.8MB
49e6a32c51e3: Pushing [=====>                                             ]  42.42MB/411.6MB
C:\Users\shahd's Laptop\bd-a1>docker push shahdhassan9903/bigdata_assignment1:tagname
550ee465949f: Pushing [=>                                                 ]  12.79MB/513.8MB
2ab1d3d1d326: Pushing [===========>                                       ]  36.18MB/150.8MB
273748eb0e4e: Pushing [=========================>                         ]  76.84MB/150.8MB
2ab1d3d1d326: Pushing [===========================>                       ]  82.41MB/150.8MB
The push refers to repository [docker.io/shahdhassan9903/bigdata_assignment1]

49e6a32c51e3: Pushing [===========>                                       ]  92.07MB/411.6MB
C:\Users\shahd's Laptop\bd-a1>docker push shahdhassan9903/bigdata_assignment1:priceless_beaver
2ab1d3d1d326: Pushing [===========================>                       ]  81.86MB/150.8MB
2ab1d3d1d326: Pushing [=========>                                         ]  28.38MB/150.8MB

C:\Users\shahd's Laptop\bd-a1>docker images
273748eb0e4e: Pushing [=========>                                         ]  29.49MB/150.8MB
273748eb0e4e: Pushing [=========>                                         ]  30.05MB/150.8MB
hello-world               latest    d2c94e258dcb   10 months ago   13.3kB
273748eb0e4e: Pushing [==========>                                        ]  30.61MB/150.8MB
273748eb0e4e: Pushing [==========================>                        ]  78.51MB/150.8MB
C:\Users\shahd's Laptop\bd-a1># Tag your Docker image
2ab1d3d1d326: Pushing [=========>                                         ]  27.26MB/150.8MB
2ab1d3d1d326: Pushing [===========================>                       ]  84.08MB/150.8MB
273748eb0e4e: Pushing [=========================>                         ]   77.4MB/150.8MB
2ab1d3d1d326: Pushing [===========================>                       ]  82.97MB/150.8MB
273748eb0e4e: Pushing [==========================>                        ]  79.07MB/150.8MB
2ab1d3d1d326: Pushing [===========================>                       ]  83.53MB/150.8MB
49e6a32c51e3: Pushing [===========>                                       ]  94.85MB/411.6MB
550ee465949f: Pushing [===>                                               ]  32.29MB/513.8MB
49e6a32c51e3: Pushing [===========>                                       ]  93.74MB/411.6MB
273748eb0e4e: Pushing [==========================>                        ]  80.19MB/150.8MB
2ab1d3d1d326: Pushing [============================>                      ]  86.87MB/150.8MB
2ab1d3d1d326: Pushing [==========================>                        ]  80.74MB/150.8MB
273748eb0e4e: Pushing [=======>                                           ]  23.37MB/150.8MB
49e6a32c51e3: Pushing [===========>                                       ]  97.08MB/411.6MB
49e6a32c51e3: Pushing [===========>                                       ]  90.95MB/411.6MB


C:\Users\shahd's Laptop\bd-a1>docker push shahdhassan9903/bd-a1:latest
The push refers to repository [docker.io/shahdhassan9903/bd-a1]
273748eb0e4e: Pushing [=======>                                           ]  22.81MB/150.8MB
2ab1d3d1d326: Pushing [========>                                          ]  25.04MB/150.8MB
4aca3f2b659b: Pushed
550ee465949f: Pushing [>                                                  ]  9.446MB/513.8MB
49e6a32c51e3: Pushing [====>                                              ]  35.18MB/411.6MB
5498e8c22f69: Mounted from library/ubuntu

____________________________________________________________________________________________________
* Bash Files Created:
----------------------
final.sh --> to move the output files to the local machine
files.sh --> to move the python files to the local machine
____________________________________________________________________________________________________

* Docker Hub repo:
https://hub.docker.com/repository/docker/shahdhassan9903/bigdata_assignment1/general

* Github repo:
https://github.com/Shahd-Hassan/BigData_Asssign1-
____________________________________________________________________________________________________
* The Execution of the project:
--------------------------------
- Created a directory named "bd-a1"
- move into /home/doc-bd-a1/
- build a docker image and work inside a container
- load the dataset into the container
- worked on the dataset (preprocessing, eda, visualization, k-means,...) by creating python files to apply these techniques
- created two bash files to move both the ouputs and the python files from the container to the local machine
- pushed the image to docker hub 
- pushed the project to github
- created a readme.md file to describe the project
- The output icluded:
1. 3 text files that had the insights of the eda.
2. Histogram plot of the dataset (visualization)
3. preprocessed data
4. the k mean algorithm 
____________________________________________________________________________________________________________________

* License :
[MIT](https://choosealicense.com/licenses/mit/)











