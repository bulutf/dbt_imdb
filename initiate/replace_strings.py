
with open('temp.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace(';', ',')

# Write the file out again
with open('250imdbtooltemp.txt', 'w') as file:
  file.write(filedata)


# columns with commas; country,genre,imdbvotes,language,actors
# get them in quotation marks