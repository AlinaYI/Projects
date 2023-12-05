content = ["All carrots are to be sliced longitudinally.",
           "The carrots were reportedly sliced.",
           "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

'''
write program that generate three files with corresponding content in folder files
'''

for content, filenames in zip(content,filenames):
    file = open(f"../files/{filenames}", 'w')
    file.write(content)
