cd files
pwd
cp -a ./template sessions/tmp
cd sessions/tmp
mv ../../image.zip image.zip && mv ../../report.md report.md
unzip -o image.zip
make
cd ../../
mv sessions/tmp sessions/{time_now}
