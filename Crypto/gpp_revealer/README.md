# GPP Revealer - Tool to Decrypt Group Policy Preferences Passwords

---

## Overview

**GPP Revealer** is a lightweight tool designed to decrypt the **cpassword** values stored in Microsoft Group Policy Preferences (GPP) XML files. These passwords are encrypted with a well-known (leaked) AES key and can be recovered in cleartext, representing a critical security risk in Active Directory environments.

---

## Features

- Parse XML files containing GPP user/group password data
- Decrypt `cpassword` fields using the official AES key and IV
- Output usernames and decrypted passwords clearly
- Supports batch processing of multiple users in a single XML
- Minimal dependencies, easy to run in any Python 3 environment

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/gpp-revealer.git
cd gpp-revealer
```

2. Install dependencies

```bash

pip install pycryptodome
```

## Usage

```bash
python gpp_revealer.py /path/to/XXXX.xml
```

## Supported Files

    Groups.xml

    Drives.xml

    Services.xml

    ScheduledTasks.xml

    Printers.xml

Any GPP XML file containing cpassword attributes.


