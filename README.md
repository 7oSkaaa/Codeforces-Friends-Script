# Codeforces Friends Script

## Requirements

### Linux User

```shell
# installing python
sudo apt install python3
```

```shell
# installing pip
sudo apt install python3-pip
```

### Windows User

1. **Windows user can install python3 from [here](https://www.python.org/downloads/)** and make sure that you will check the option `Add Python 3.x to PATH` while installing and .

2. **Install pip** from [here](https://pip.pypa.io/en/stable/installation/)

## Installing

```shell
# downloading the script
git clone https://github.com/7oSkaaa/Codeforces-Friends-Script.git
```

or you can download the script from [here](https://github.com/7oSkaaa/Codeforces-Friends-Script/archive/refs/heads/main.zip)

***open your terminal and run these commands***

```shell
# open the folder of the script
cd Codeforces-Friends-Script
```

```shell
# downloading the requirements and updating them
pip install --upgrade -r requirements.txt
```

## Usage

1. Rename `.env.example` to `.env` and fill the data:
   1. CF_HANDLE: your codeforces handle
   2. CF_PASSWORD: your codeforces password
   3. REMOVE_EXIST_FRIENDS: True or False
      1. True: remove the existing friends and add the new ones
      2. False: add the new friends without removing the existing ones
2. open your terminal and run this command:

    ```shell
    # run the script
    python3 main.py
    ```

3. **Enjoy!**

## Note

- if the script take 10 seconds without printing anything, close the script and run it again.
  - this problem is caused by the codeforces website, it's not a problem with the script.
