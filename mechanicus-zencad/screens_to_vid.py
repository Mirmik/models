#!/usr/bin/env python3

import moviepy
import moviepy.editor

images = ["screens/an{}.jpg".format(i) for i in range(0,4250) ]
#images = ["screens/an{}.jpg".format(i) for i in range(0,512) ]
clip = moviepy.editor.ImageSequenceClip(images, fps=24)
clip.write_videofile("video.mp4")
