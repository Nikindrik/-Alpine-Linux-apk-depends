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

# 💻 Command in UNIX emulation

* **Displays available commands and their brief descriptions** - `help`
* **Lists directories and files in the current working directory** - `ls`
* **Changes the current directory in the virtual filesystem** - `cd`
* **Exits the emulator or application** - `exit`
* **Counts words, lines, or characters in a file** - `wc`
* **Moves or renames files or directories** - `mv`
* **Clears the console output screen** - `clear`

# 🖼️ Gallery

![img.png](source/img/img.png)

![img.png](source/img/img_2.png)
