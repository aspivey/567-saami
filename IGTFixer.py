# -*- coding: utf-8 -*-
#requires Python3
import re

def main():

    #The list of UTF-8 characters you want replaced with the ascii representations you've chosen.
    #If you have double characters (like ŋŋ to signal gemination) putting them first in the array should make sure ŋŋ is resolved before ŋ.
    #But I haven't actually tested that. 
    replaceTable = [("å","ao"), ("á","aa"), ("ä","ae"), ("ŋŋ","nng"), ("ŋ","ng")]

    #Run forever
    while True:
        #Any copy/pasted input needs to be preceded by three quotes and followed by three more to close it off.
        #This makes it so that you can paste paragraphs and still have python swallow the whole thing. 
        igt = input("Type \"\"\" and then paste igt:")

        reformatted = [[],[],[],[]]

        #replace all non-ascii characters
        for transcription in replaceTable:
            print(transcription)
            igt = re.sub(transcription[0], transcription[1], igt)

        #The Pite Saami documentation has things like moose\nom\sg. This gets rid of
        #computer-unfriendly backslashes and replaces them with forward slashes. 
        igt = igt.replace("\\", "/")
        igt = igt.split("\n")
        #strip off the sentence at the end. At least in our documentation, the english translation is on its own line, so we're going to strip it off and print it alone. 
        sentence = igt[-1]
        igt = igt[:-1]

        #Skip through the interleaved IGT and collect it into arrays that group it together. 
        index = 0

        while index < len(igt):
            reformatted[0].append(igt[index])
            index += 3

        index = 1

        while index < len(igt):
            reformatted[1].append(igt[index])
            index += 3

        index = 2
        
        while index < len(igt):
            reformatted[2].append(igt[index])
            index += 3

        #Print it all out.     
        for line in reformatted:
            print("\t".join(line))
        print(sentence)




main()
