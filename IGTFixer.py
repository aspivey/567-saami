# -*- coding: utf-8 -*-
import re

def main():

    replaceTable = [("å","ao"), ("á","aa"), ("ä","ae"), ("ŋŋ","nng"), ("ŋ","ng")]

    while True:
        igt = input("Type \"\"\" and then paste igt:")

        reformatted = [[],[],[],[]]

        for transcription in replaceTable:
            print(transcription)
            igt = re.sub(transcription[0], transcription[1], igt)
        
        igt = igt.replace("\\", "/")
        igt = igt.split("\n")
        sentence = igt[-1]
        igt = igt[:-1]

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
            
        for line in reformatted:
            print("\t".join(line))
        print(sentence)




main()
