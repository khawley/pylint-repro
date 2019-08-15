# Summary

For unknown reasons, pylint is behaving differently based on different operating systems.

# Steps to Reproduce

1. Setup a virtualenv with Python 3.6.8.

2. Pip install pylint 2.3.0.

```
pip install pylint==2.3.0
```

3. Run pylint on the main_file.py

```
pylint sub/main_folder/main_file.py
```

4. Experience a pylint error, flavored by your OS. 

Running python 2.7.12 w/ pylint 1.9.5 on Mac
```bash
» pylint sub/main_folder/main_file.py
No config file found, using default configuration
************* Module sub.main_folder.main_file
E:  6, 0: Module 'sub.other_folder.module' has no 'Module' member (no-member)
```

Running python 3.6.8 w/ pylint 2.3.0 on Mac
```bash
» pylint sub/main_folder/main_file.py
************* Module sub.main_folder.main_file
sub/main_folder/main_file.py:6:0: E1102: module.Module is not callable (not-callable)
```

Running python 3.6.8 on Linux
```bash
$ pylint --version
pylint 2.3.0
astroid 2.2.5
Python 3.6.8 (default, Aug 15 2019, 13:29:58)g
[GCC 9.1.0]
$ pylint sub/main_folder/main_file.py
************* Module sub.main_folder.main_file
sub/main_folder/main_file.py:6:0: E1101: Module 'sub.other_folder.module' has no 'Module' member (no-member)

----------------------------------------------------------------------
Your code has been rated at -15.00/10 (previous run: -15.00/10, +0.00)
```

# Table of errors + versions

OS|python|pylint|lint error
--|------|-------|----------
Mac 10.14.5|2.7.12|1.9.5|no-member
Mac 10.14.5|3.6.8|1.9.5|not-callable
Mac 10.14.5|3.6.8|2.3.0|not-callable
Mac 10.14.5|3.6.8|2.3.1|not-callable
Mac 10.14.5|3.7.3|2.3.0|not-callable
Arch Linux|2.7.12|1.9.5|no-member
Arch Linux|2.7.16|1.9.5|no-member
Arch Linux|3.6.7|1.9.5|no-member
Arch Linux|3.6.8|1.9.5|no-member
Arch Linux|3.6.7|2.3.0|no-member
Arch Linux|3.6.8|2.3.0|no-member
