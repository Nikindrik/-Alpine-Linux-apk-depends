<h1 align="center"> Alpine Linux apk depends  </h1>
This is a command line tool for visualizing dependency graph. Dependencies are identified by the Alpine Linux OS package name (apk). Graphviz representation is used to describe the dependency graph. The visualizer outputs the result as a graphical representation of the graph.

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

# 💻 The command line switches are set:

* **Path to graph visualization program.**
* **The name of the packet being analyzed.**
* **Repository URL.**

# 🖼️ Results Gallery

![img.png](source/img/img_1.png)

![img.png](source/img/img_2.png)
