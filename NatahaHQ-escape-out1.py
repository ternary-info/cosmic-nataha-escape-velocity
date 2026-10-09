#!/usr/bin/python
#
# THIS CODE IS PUBLIC DOMAIN - USE IT ON YOUR OWN RISK!
#
# Based on NatahaHQ script created in February 2026 by Shaos
#
import os,sys,shutil

prefix = "NatahaHQ-escape-out1"
prefix1 = "NatahaHQ-escape-v03/"
prefix2 = "NatahaHQ-escape-v12/"
prefix3 = "NatahaHQ-escape-v13/"
prefix4 = "NatahaHQ-escape-v15/"
prefix5 = "NatahaHQ-escape-v16/"
prefix6 = "NatahaHQ-escape-v18/"
prefix7 = "NatahaHQ-escape-v19/"
globalf = 29.97
globali = 0
globalt = 0.0
localt = 0.0

# Clean the output directory from the previous run
if os.path.exists(prefix):
    shutil.rmtree(prefix)
os.makedirs(prefix)

def conv3(pref,i,f):
 global globalf,globali,globalt,localt
 st = "%.6d" % (i)
 localt += 1.0/f
 while globalt < localt :
    globali += 1
    st1 = "/%.6d" % (globali)
    print pref + st + " -> " + st1 + " fps=" + str(f) + " t=" + str(globalt) + " (" + str(localt) + ")"
    globalt += 1.0/globalf
    os.system("cp " + pref + st + ".jpg " + prefix + st1 + ".jpg")

for j in (range(65,109)):
  conv3(prefix1,j,27)
for j in (range(109,161)):
  conv3(prefix1,j,24)

for j in (range(1,61)):
  conv3(prefix2,j,21)

for j in (range(1,39)):
  conv3(prefix3,j,37)
for j in (range(39,90)):
  conv3(prefix3,j,25)
for j in (range(90,173)):
  conv3(prefix3,j,23)

for j in (range(20,62)):
  conv3(prefix4,j,27)
for j in (range(62,79)):
  conv3(prefix4,j,60)
for j in (range(79,107)):
  conv3(prefix4,j,23)
for j in (range(107,115)):
  conv3(prefix4,j,12)
for j in (range(115,143)):
  conv3(prefix4,j,50)
for j in (range(143,193)):
  conv3(prefix4,j,27)


for j in (range(62,82)):
  conv3(prefix5,j,22)
for j in (range(117,193)):
  conv3(prefix6,j,50)
for j in (range(22,90)):
  conv3(prefix5,j,20)
for j in (range(90,150)):
  conv3(prefix5,j,25)
for j in (range(150,193)):
  conv3(prefix5,j,32)

for j in (range(1,193)):
  conv3(prefix7,j,28)
for j in (range(25,95)):
  conv3(prefix6,j,24)

os.system("mencoder \"mf://" + prefix + "/*.jpg\" -mf fps=29.97 -audiofile escape1.wav -oac pcm -ovc lavc -lavcopts vcodec=mpeg4:vbitrate=12000 -o " + prefix + ".avi")
os.system("mplayer " + prefix + ".avi")
