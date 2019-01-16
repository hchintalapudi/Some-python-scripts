#!/usr/bin/python

#This program takes a BED file and splits it into separate BED files per chromosome 

#importing required packages to run command line parameters
import argparse
   
def run(args):      
    bed_file = open(args.bed_file)
    file_list = {}
    for line in bed_file:
        
        #split the bed file
        fields = line.split()

        #check if chromosome file exists, if not, create it.
        if fields[0] not in file_list:
            file_name = str('bed' + '_' + str(fields[0]))
            file1 = open('%s.bed' %(file_name), 'w+')
            file_list[fields[0]] = file1

            #write lines to the chromosome file 
            file_list[fields[0]].write(line)
    # close files
    for key, value in file_list.iteritems():
        value.close
    bed_file.close

#function to add the argparse command line arguments
def main():
    parser = argparse.ArgumentParser(description = "Splits given BED file to separate BED files per chromosome")
    parser.add_argument("-b","--BED_file", action = "store",dest = "bed_file", help = "BED file to be split.", required = True)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()


