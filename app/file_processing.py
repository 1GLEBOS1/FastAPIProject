from os import system as term
from time import time

def make():
    term("""cd ../files
        cp -a ./template sessions/tmp
        mv downloads/image.zip sessions/tmp/image.zip && mv downloads/report.md sessions/tmp/report.md
        cd sessions/tmp && unzip -o image.zip
        make
        """)
    time_now = time()
    term(f"""cd ../files
        mkdir -p downloads/{time_now}
        mv sessions/tmp/report.pdf downloads/{time_now}/report.pdf
        mv sessions/tmp/report.docx downloads/{time_now}/report.docx
        rm -rf sessions/tmp
        """)
    return time_now
