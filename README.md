# :alien: Assignment 1 - Help John with Parallel Programming! :fire::dancer:

![image](https://www.ictshore.com/wp-content/uploads/2018/03/py0009-00-Python_threading_tutorial.png)

John is a data engineer who works at Lola Inc. He wants to download some pictures from internet, and resize them, however, his process takes a lot of time as the number of images increases. He asks your help, to speed up his process.

## The Goal

The goal is to achieve concurrent programming using Python. This project shows you the two ways of parallelising tasks, in which you have to improve the speed of the serial-programming application by using threading and/ or multiprocessing.

Things to remember, 

1. IO bound operations requires threading
2. CPU bound operations requires multiprocessing

There are many options for multithreading and multiprocessing. You are more than welcome to choose any of those libraries including the standard packages. My advise is to test diffrent ones, so that you will cover more.

Some of these packages are, but not limited to:

- [Ray](https://github.com/ray-project/ray)
- [Numba](http://numba.pydata.org/)
- [Modin](https://github.com/modin-project/modin)
- [Dask](https://dask.org/)
- [multiprocessing](https://docs.python.org/3.8/library/multiprocessing.html)
- [threading](https://docs.python.org/3.8/library/threading.html)
- [concurrent.futures](https://docs.python.org/3.8/library/concurrent.futures.html)

These packages have advantages and disadvantages, you may look more into examples in internet.

## How to do the Assignment?

Use the link given in the class to create your repository. The link will automatically create a repository for you with this assignment template, so you may proceed to the following list.

The same procedure for [welcome](https://github.com/spu-bigdataanalytics/welcome) assignment remains the same, where you have to rename this file as Instructions.md, and create a new README.md file with your own description. In this description, you may explain which methods you choose and why, you can give more examples, and explain how the code you wrote works. Remember, the purpose of this file is afterall for other people to understand what you have done with your project! Plus, without README.md, you may not get a full grade.

1. Get an Imgur api key. Follow instructions [here](https://apidocs.imgur.com/?version=latest#intro).
2. Install requirements.txt in your environment. (`pip install -r requirements.txt`)
3. Launch Jupyter Notebook.
4. Do assignment!
5. Write an authentic README.md.


## What are all these other files?

Following table is will give it a meaning for each file.

File | Description |
---- | ----------- |
README.md ** | A descriptive file to give an introduction of current project/ assignment. 
Instructions.md ** | A copy of current README.md file. 
LICENCE ** | The licence of the file that every project should have.
.gitignore | The file to control which files should be ignored by Git.
images | The downloads folder of where your hw downloads the images to.
requirements.txt | The packages needed to run this project. You may use `pip` to install these packages.
config.txt | This file is your configuration file. Imgur needs Client ID key to be provided. Put your key in this file.
utils.py | The helper module that John uses to complete the task.
Assignment1.ipynb | The assignment notebook. You will find more instructions in this assignment.


## How to submit the assignment?

Submit is very easy! You just have to do two things.

1. You have to do your latest commit before the deadline!
2. After you finish, download a zip copy of your project, upload it to Blackboard!