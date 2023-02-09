
# Import a file and and re-format as required 

import csv

infile = "Scheulde.csv"
outfile = "output1.csv"

with open(infile, 'r') as in_file:
    output = ""
    for line in in_file:

        stripped = line.strip()
        stripped = stripped.replace('-', ',').title()
        stripped = stripped.replace('Wap', 'WAP')
        stripped = stripped.replace('Cam', 'CAM')
        stripped = stripped.replace('Hdbaset', 'HDbaseT')
        stripped = stripped.replace('Tv', 'TV')
        stripped = stripped.replace('Or', 'or')
        stripped = stripped.replace('Fb', 'Floor Box')
        stripped = stripped.replace('Ugc', 'Underground Cable')
        stripped = stripped.replace('Lvl', 'LVL')
        stripped = stripped.replace('Ts', 'Touch Screen')
        stripped = stripped.replace('Ens', 'ENS')
        stripped = stripped.replace('Wir', 'WIR')
        stripped = stripped.replace('Ac', 'AC')
        stripped = stripped.replace('At', 'at')
        stripped = stripped.replace('Of', 'of')
        stripped = stripped.replace('Gf', 'GF')
        stripped = stripped.replace('1Fl', '1FL')
        stripped = stripped.replace('Bbq', 'BBQ')
        stripped = stripped.replace('Util', 'UTIL')
        stripped = stripped.replace('Play Rm', 'Rumpus')
        stripped = stripped.replace('Ext', 'EXT')


        stripped += "\n"

        output += stripped

    print(output)

    with open(outfile, 'w') as f:
        f.write(output)


       