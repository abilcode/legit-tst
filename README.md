## Setup

Start the project with environment setup and run the jupyterlab

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


next just jump right to the app file