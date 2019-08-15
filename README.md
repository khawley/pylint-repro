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
