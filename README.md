# Megapy

A simple client to wrap the [MEGAcmd](https://github.com/meganz/MEGAcmd) CLIs on the **Mega** class.
- It is not a complete wrapper to all CLIs and it is not meant to be.

---

### How to install and use this package:
1. Use pip to install, you can install using this repo HTTPS or SSH URL, but in any case, you must have permission to clone this repo:
```sh
# SSH
pip install git+ssh://git@github.com/diogovalentte/megapy.git#egg=megapy --upgrade

# HTTPS
pip install git+https://{YOUR TOKEN}@github.com/diogovalentte/megapy.git#egg=megapy --upgrade
```
2. (Optional) If you're logged in the MEGAcmd (like using the commnad `mega-login` to login with your Mega account), this library will use your account.
3. It's a simple package, just look in the **src/** folder to know how to use it.
