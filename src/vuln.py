import os

def check_input(user_input):
    # This should trigger the Semgrep rule we added
    eval(user_input)

def run_command(cmd):
    os.system(cmd)
