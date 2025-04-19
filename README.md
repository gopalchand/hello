# hello_cmake
An example of a minimal Python "Hello, World!" project that can be installed using pip install from a GitHub repo — and uses CMake to build a native Python extension (e.g., a C++ backend).
This is often done when you want to integrate C++ performance into Python.

Testing with Windows 11. Below are instructions of how this repo was set up including information/reminders for how to get started with with GitHub and repos.

Folder Structure:
hellothere_project/
├── CMakeLists.txt
├── pyproject.toml
├── setup.py
├── src/
│   ├── hello.cpp
│   └── hello.hpp
├── python/
│   └── hellothere_package/
│       ├── __init__.py
│       └── hellothere_bindings.cpp

## 0. Preparation
Optional installation of packages
```
pip install --upgrade pip setuptools wheel
pip install scikit-build cmake ninja pybind11
```

## 1. Initialize Git (if not already done)
This creates a new repository - usually the first command for a new project
```
git init
```

## 2. Add the remote origin (replace with your actual username!)
Add the remote repository to a local Git repository. "origin" is an alias for the remote repository URL that can b used subsequently
```
git remote add origin https://github.com/gopalchand/hellothere_project.git
```
Validate with the following:
```
git remote -v
origin  https://github.com/gopalchand/hello.git (fetch)
origin  https://github.com/gopalchand/hello.git (push)
```

## 3. Add and commit your files
Select changes using add and then commit *locally* using "-m" for the text associated with the change(s)
```
git add .
git commit -m "Initial commit with CMake Python extension"
```

## 4. Push to GitHub
Rename the current branch to main and force-push it to GitHub (typically for first-time setup):
```
git branch -M main
git push -f origin main
```
-f (force) intentionally overwrites the remote main branch.

## 5. Change email to noreply email using https://www.github.com/emails for details
If you see the error "Your push would publish a private email address." (see https://www.github.com/emails), use the appropriate noreply email and update the config:
```
git config --global user.email "12345678+yourusername@users.noreply.github.com"
git commit --amend --reset-author
```
## 6. Push amny subsequent changes
After editing files, stage the changes, commit with a meaningful message, and push:
```
git add .
git commit -m "change description"
git push origin main
```

## 7. Install
```
pip install git+https://github.com/gopalchand/hellothere_project.git
```

## 8. Typical output (Windows 11):
The pip install git+https://github.com/user/repo.git usually does the following:
```
git clone https://github.com/user/repo.git <local_folder>
```
cd into the <local_folder>
if there's a pyproject.toml present then install everything in the requires=[...] part and then call setuptools.build_meta which is patched by scikit-build. scikit_build runs CMake and Ninja to compile C++ code and install the .pyd and __init__.py (from .<module> import <function>) into the Python package via install() in CMake run from scikit-build e.g. for Python 3.10 under Windows x64:

%LOCALAPPDATA%\Programs\Python\Python310\Lib\site-packages\
└── hellothere_package\
    ├── __init__.py
    └── hellothere_module.cp310-win_amd64.pyd

This will allow import hellothere_package to work along with calling hellothere_package.say_hello() (<module>.<function>)

In addition setuptools.build_meta looks at setup.py for information about the package (name, version, package and package_dir etc.).

Example output:
```
pip install git+https://github.com/gopalchand/hellothere_project.git
Looking in indexes: https://pypi.org/simple, https://pypi.ngc.nvidia.com
Collecting git+https://github.com/gopalchand/hellothere_project.git
  Cloning https://github.com/gopalchand/hellothere_project.git to %TEMP%\pip-req-build-d3woeokv
  Running command git clone --filter=blob:none --quiet https://github.com/gopalchand/hellothere_project.git '%TEMP%\pip-req-build-d3woeokv'
  Resolved https://github.com/gopalchand/hellothere_project.git to commit 507725bea2010196f879a3e057d4ea41af190ba1
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: hellothere_package
  Building wheel for hellothere_package (pyproject.toml) ... done
  Created wheel for hellothere_package: filename=hellothere_package-0.1-cp310-cp310-win_amd64.whl size=53367 sha256=3fedabd8a4d89274503e7b02e7b101cf629f2db0464e973879caccce3f3c56e4
  Stored in directory: %TEMP%\pip-ephem-wheel-cache-jge77pdn\wheels\9a\0c\db\b48906b275a2abdf1bf466b67ab79beabdc3758ba57ec41dc2
Successfully built hellothere_package
Installing collected packages: hellothere_package
Successfully installed hellothere_package-0.1
```

## 10. Check installation
```
pip list|grep hellothere_package
hellothere_package                0.1

```

## 11. Import and test
```
import hellothere_package
print(hellothere_package.say_hello())
```

Thanks to [ChatGPT](https://chat.openai.com) for guidance on setting up this CMake + pybind11 + scikit-build Python package.

