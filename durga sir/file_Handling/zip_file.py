from zipfile import ZIP_DEFLATED, ZipFile

f=ZipFile("file_Handling/zip_file.zip","w",ZIP_DEFLATED)
f.write("file_Handling/file.txt")
# f.write("file_Handling/1st_csv.csv")
# f.write("file_Handling/Guido.jpg")
# f.write("file_Handling/write.csv")

print("File Created Successfully")