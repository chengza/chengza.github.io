我的这个静态博客为了方便起见使用的是python脚本做了简单的打包工作，将md文件转换成html最后整理打包上传到github。其中依赖了markdown库，如果迁移到别的电脑上使用就不仅仅需要安装python，还要安装markdown库，这不方便。

使用pyinstaller可以把python程序打包成exe或者unix执行程序。安装过程不介绍了，就是使用pip而已。

由于本身依赖项比较少，代码不复杂，直接使用一行命令简单打包。

```
pyinstaller -F do-commit.py
```

稍等片刻，虽然其中有一些warning，不过最后还是成功生成了。看一下现在的目录结构。

```
│   .gitignore
│   do-commit.py
│   do-commit.spec 
│   index.html
│
├───.idea
│   │   .gitignore
│   │   chengza.github.io.iml
│   │   deployment.xml
│   │   misc.xml
│   │   modules.xml
│   │   vcs.xml
│   │   workspace.xml
│   │
│   └───inspectionProfiles
│           profiles_settings.xml
│           Project_Default.xml
│
├───build
│   └───do-commit
│           Analysis-00.toc
│           base_library.zip
│           do-commit.exe.manifest
│           do-commit.pkg
│           EXE-00.toc
│           PKG-00.toc
│           PYZ-00.pyz
│           PYZ-00.toc
│           Tree-00.toc
│           Tree-01.toc
│           Tree-02.toc
│           warn-do-commit.txt
│           xref-do-commit.html
│
├───dist
│       do-commit.exe
│
├───html
│       使用pyinstaller打包Python程序.html
│
├───posts
│       使用pyinstaller打包Python程序.md
│
└───PP
    │   index.html
    │
    ├───css
    │       index.css
    │       reset.css
    │
    ├───js
    │       index.js
    │
    └───media
            avatar.png
            myWechat.jpg
```

虽然比起我以前做的另一个使用java写的打包程序还是简陋了一些，不过不得不承认，python很方便，至少写的时候很方便。改的时候……那就等改的时候再骂它吧，哈哈。
