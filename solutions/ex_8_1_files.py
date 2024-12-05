# Write a function grep that receives text and file as parameters and returns
# a list with all the lines in the file containing text.
def grep(text, file):
    lines_matching = []
    with open(file) as f:
        for line in f:
            if text in line:
                lines_matching.append(line)
    return lines_matching


print(grep("better", "infile.txt"))


# Write another function grepinto that receives text, infile and outfile as
# parameters and writes to outfile the lines in infile that contain text. Open
# both files within one with statement.
def grepinto(text, infile, outfile):
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        for line in fin:
            if text in line:
                fout.write(line)


grepinto("better", "infile.txt", "outfile.txt")
