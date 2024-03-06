"""

-- main.py

This file is the main file for the project. It contains the main code and will run when the program runs.

"""

import os
import sys
import platform
# import tkinter as tk -- Don't know if I will make a tk GUI

class Permissions:
    def print_system_info():
        uname = platform.uname()
        print("="*40, "System Information", "="*40)
        print(f"System: {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")

Permissions.print_system_info()