#!/usr/bin/env python3
from moviepy.editor import *
import os

files = os.listdir("screens")

def keyfunc(x):
	p, e = os.path.splitext(x)
	return int(p[2:])

files = sorted(files, key=keyfunc)
files = [os.path.join("screens",f) for f in files]

clip = ImageSequenceClip(files, fps=50)

clip.write_videofile("robot.mp4")