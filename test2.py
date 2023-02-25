filenames = ['1.Doc', '1.report', '1.presentaion']

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)


