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
python main.py <package_name> <repo_url>
```
Example 
```editorconfig
python main.py busybox-extras-openrc "https://pkgs.alpinelinux.org"
```