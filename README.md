<h1 align="center"> Alpine Linux apk depends  </h1>
Some info

# 📘 Installation and running

```commandline
git clone https://github.com/Nikindrik/-Alpine-Linux-apk-depends
python -m venv venv
```
For windows
```commandline
.\venv\Scripts\activate
pip3 install requests
pip3 install bs4
```
For linux/UNIX/MAC
```commandline
source venv/bin/activate
pip3 install requests
pip3 install bs4
```
Run
```commandline
python main.py --user <user_name> --archive <archive_name.zip> --script <start_script_name.sh>
```
Example 
```editorconfig
python main.py --user nick --archive systeam.zip --script start.sh
```