# hello_cmake
An example of a minimal Python "Hello, World!" project that can be installed using pip install from a GitHub repo — and uses CMake to build a native Python extension (e.g., a C++ backend). 
This is often done when you want to integrate C++ performance into Python.

## 0. Preparation
```
pip install --upgrade pip setuptools wheel
pip install scikit-build cmake ninja pybind11
```

## 1. Initialize Git (if not already done)
```
git init
```

## 2. Add the remote origin (replace with your actual username!)
```
git remote add origin https://github.com/gopalchand/hello_cmake.git
```

## 3. Add and commit your files
```
git add .
git commit -m "Initial commit with CMake Python extension"
```

## 4. Change email to noreply email using https://www.github.com/emails for details
```
git config --global user.email "12345678+yourusername@users.noreply.github.com"
git commit --amend --reset-author
```

## 5. Push to GitHub
```
git branch -M main
git push -f origin main
```

## 6. Push amny changes
```
git add .
git commit -m "change description"
git push origin main
```

## 7. Install
```
pip install git+https://github.com/gopalchand/hello_cmake.git
```

## 8. Typical output:
```
Looking in indexes: https://pypi.org/simple, https://pypi.ngc.nvidia.com
Collecting git+https://github.com/gopalchand/hello_cmake.git
  Cloning https://github.com/gopalchand/hello_cmake.git to <TEMPDIR>\pip-req-build-d6gnanpm
  Running command git clone --filter=blob:none --quiet https://github.com/gopalchand/hello_cmake.git '<TEMPDIR>\pip-req-build-d6gnanpm'
  Resolved https://github.com/gopalchand/hello_cmake.git to commit 202852a941506ee344902110252e777690da7b1c
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: hello_cmake
  Building wheel for hello_cmake (pyproject.toml) ... done
  Created wheel for hello_cmake: filename=hello_cmake-0.1.0-cp310-cp310-win_amd64.whl size=53218 sha256=c9e4124ccf0b5ba682b7479553a349dd8c54ed0f5643a06fb30dc774a2a57209
  Stored in directory: <TEMPDIR>\pip-ephem-wheel-cache-l8eqnk2y\wheels\92\b6\f7\dfb02c33d77e726ce764b76278808d641bb4d1129683032c58
Successfully built hello_cmake
Installing collected packages: hello_cmake
Successfully installed hello_cmake-0.1.0
```

## 10. Check installation
```
pip list|grep hello_cmake
hello_cmake                       0.1.0
```

## 11. Import and test
```
import hello
print(hello.say_hello())
```



