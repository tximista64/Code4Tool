# ASM Toolkit 

##  Description

This folder contains a custom toolkit for working with **Assembly code**, including:

- A minimalist **assembler/linker** to convert assembly into raw binaries or shellcode.
- Python scripts to **generate shellcode** from assembly and to **decompile shellcode** back into human-readable ASM.
- Useful for **exploit development**, **reverse engineering**, and **binary analysis**.

##  Structure

```bash
ASM/
├── Ceasar.sh/                # Assemble and link file 
├── loader.py                 # Allows you to execute shellcode by passing it as a hexadecimal string.
├── shellcode2assembler.py.py # Disassembles shellcode into ASM
├── shellcoder.py             # Extract shellcodes from elf files
├── shellcoder.sh             # Same stuff in bash
└── README.md

