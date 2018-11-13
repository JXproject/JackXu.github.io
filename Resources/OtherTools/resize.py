#!/usr/bin/env python

from PIL import Image
import os, sys

def resizeImage(infile, output_dir=""):
     outfile = os.path.splitext(infile)[0]+"_min"
     extension = os.path.splitext(infile)[1]
     w=1024
     if (cmp(extension, ".jpg")):
        return

     if infile != outfile:
        try :
            im = Image.open(infile)
            width, height = im.size
            if(width>height):
                nh = width*height/w
            else:
                nh = w
                w = height*width/nh
            im.thumbnail((w, nh), Image.ANTIALIAS)
            im.save(output_dir+outfile+extension,"JPEG")
        except IOError:
            print "cannot reduce image for ", infile


if __name__=="__main__":
    output_dir = "min/"
    dir = "./"

    if not os.path.exists(os.path.join(dir,output_dir)):
        os.mkdir(output_dir)

    for file in os.listdir(dir):
        resizeImage(file,output_dir)