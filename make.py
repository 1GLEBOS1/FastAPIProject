import os


def make():
    os.system("cd files && unzip -o image.zip")
    os.system("cd files && make")
