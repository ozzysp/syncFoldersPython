# syncFoldersPython


This Python script was made by Ozzy for test purposes.

The objective of this project is to create a simple application that synchronizes between 2 pre-selected folders in the system.

## First time setup
- Fork synchFoldersPython to your GitHub account by clicking the `Fork` button.

- Clone the main repository locally.
```
$ git clone https://github.com/ozzysp/syncFoldersPython
$ cd syncFoldersPython
```

- Add your fork as a remote to push your work to. Replace {username} with your username. This names the remote "fork", the default AlphaCopy remote is "origin".
```
$ git remote add fork https://github.com/{username}/syncFoldersPython
```

- Create and activate a virtualenv.
### Linux/Mac
```
$ python3 -m venv .venv
$ source .venv/bin/activate
```
### Windows
```
$ pip3 install virtualenv
$ virtualenv {virtualenv-name}
$ {virtualenv-name}\Scripts\activate
```

- Install in editable mode with development dependencies.
```
$ pip install -r requirements.txt
```


## Start coding
- Create a branch to identify the issue you would like to work on. If you're submitting a bug or documentation fix, branch off of the latest ".x" branch.

```
$ git fetch origin
$ git checkout -b your-branch-name origin/1.1.x
```

If you're submitting a feature addition or change, branch off of the "master" branch.
```
$ git fetch origin
$ git checkout -b your-branch-name origin/master
```

- Using your favorite editor, make your changes, committing as you go.

- Include tests that cover any code changes you make. Make sure the test fails without your patch. Run the tests as described below.

- Push your commits to your fork on GitHub and create a pull request. Link to the issue being addressed with fixes #123 in the pull request.
```
$ git push --set-upstream fork your-branch-name
```

## How to use

Open a Terminal window and navigate to syncoFoldersPython.py.
Enter the following command for Windows  ++python syncFoldersPython.py and hit "enter" key.
In Unix based systems the command is ++python3 syncFoldersPython.py and hit "enter" key.
Now terminal will show a prompt for your source directory, choose a target directory giving a correct absolute path to command and hit "enter" key.
You'll prompted to type a path for replica directory, again choose an absolute path to this directory and hit "enter" key.
The new prompt will ask for log file, choose am absolute path to this directory and hit "enter" key.
Last, a prompt for synchronize time interval will be displayed, choose a time in minutes and hit "enter" key.
Now, the script will run and show results of your job in terminal and will save log.txt with time of each backup made. 
To stop the script, only close Teminal windows and the program will stop.


# Thank you for your attention!
