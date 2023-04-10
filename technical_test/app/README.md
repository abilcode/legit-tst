## Setup

Start the project with environment setup and run the jupyterlab, or make sure u already installed the dependency

```
pip install virtualenv
virtualenv legit-tst-env
source legit-tst-env/bin/activate
pip install -r requirements.txt
jupyter lab (optional)
```
or run this script for windows users
```
pip install virtualenv
virtualenv [enviroment name]
.\[enviroment name]\Scripts\activate
pip install -r requirements.txt
jupyter lab (optional)
```

After that, run this command : 
```
uvicorn main:app --reload
```

## Structure

```
    |--artifacts
    |--app
        |--data
        |--main.py
    |--code
    |--data
    |--reports
        |--figures
    |--src
```