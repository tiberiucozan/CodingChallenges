## CCWC tool by Coding Challenges

You can find the requirements and description of what the tool needs to do [here](https://codingchallenges.fyi/challenges/challenge-wc/).

### How to use this

#### Method 1: (Python 3)
Run `python3 ccwc.py -c text.txt`

#### Method 2: (bin)

1. Give the script permissions to execute by running `sudo chmod +x ccwc.py`
2. Make a hardlink of the script in your bin directory `sudo ln ccwc.py /home/user/usr/local/bin`

 On WSL you can use `sudo ln ccwc.py \\wsl.localhost\Ubuntu\usr\local\bin\ccwc`
3. Run the command `ccwc -c text.txt`

#### Method 3: (alias)
Make an alias for the command `alias ccwc='python3 /full/path/to/ccwc.py'`