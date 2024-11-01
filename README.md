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
pip3 install graphviz
```
For linux/UNIX/MAC
```commandline
source venv/bin/activate
pip3 install requests
pip3 install bs4
pip3 install graphviz
```
Run
```commandline
python main.py <graph_tool_path> <package_name> <repo_url>
```
Example 
```editorconfig
python main.py "venv\Lib\site-packages" intel-media-driver "https://pkgs.alpinelinux.org"
```