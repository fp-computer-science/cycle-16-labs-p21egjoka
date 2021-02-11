# Author: Emanuel Mark Gjoka (AMDG) 2/11/2021

ofile1 = open("my_file.txt", "w")
contents = ofile1.read
ofile1.write('''EMG, 2/11/2021
Hello World!
Reading
''')
ofile1.close()
