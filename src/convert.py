#!/usr/bin/env python3

# READING FILE TO LIST
with open("book.txt", encoding='windows-1250') as f:
    content = f.readlines()

for line in content:
        # ONLY LINES LONGER THAN 20 CHARS
        if len(line) > 20 :
                # ONLY LINES ENDING WITH NEW LINE
                if ord(line[-1]) == 10:
                        # IF BEFORE NEW LINE ARE . ! ? :
                        if ord(line[-2]) == 46 or ord(line[-2]) == 33 or ord(line[-2]) == 63 or ord(line[-2]) == 58:
                                # SAVING WITH NEW LINE
                                with open("outbook.txt", "a", encoding="utf-8") as myfile:
                                        myfile.write(line)
                                        
                        # IF BEFORE NEW LINE IS SPACE AND BEFORE SPACE ARE CHARS AS ABOVE
                        elif ord(line[-2]) == 32 and ( ord(line[-3]) == 46 or ord(line[-3]) == 33 or ord(line[-3]) == 63 or ord(line[-3]) == 58):
                                with open("outbook.txt", "a", encoding="utf-8") as myfile:
                                        myfile.write(line)

                        else:
                                with open("outbook.txt", "a", encoding="utf-8") as myfile:
                                        myfile.write( line[0:-1] )
                # OTHER LINES CUT LAST CHAR
                else:
                        with open("outbook.txt", "a", encoding="utf-8") as myfile:
                                myfile.write( line[0:-1] )
        # SHORT LINES
        else:
                with open("outbook.txt", "a", encoding="utf-8") as myfile:
                        myfile.write( line )
