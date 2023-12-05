filenames = ["1.dot", "1.report", "1.presentation"]

filenames = [filename.replace('.','-') + '.txt' for filename in filenames]

print(filenames)