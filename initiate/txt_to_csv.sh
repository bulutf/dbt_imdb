
# create empy .txt file
touch 250imdbtooltemp.txt

# replace needed strings
python comma.py
python replace_strings.py

# move csv to the data folder
mv 250imdbtooltemp.txt ../data/SOURCE_IMDB.csv

# change encoding to UTF-8
iconv -f ISO-8859-1 -t UTF-8//TRANSLIT ../data/SOURCE_IMDB.csv > ../data/250imdbtool.tmp; mv ../data/250imdbtool.tmp ../data/SOURCE_IMDB.csv

# feed the database wtih csv
dbt seed
