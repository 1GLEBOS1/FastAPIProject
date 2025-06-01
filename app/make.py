from os import system as term


def make():
    term("cd ../files && unzip -o image.zip")
    term("cd ../files && make")
