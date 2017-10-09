# Usage: ./make_corpus.sh corpus_name
# Dumps content of all the tmx files of current dir into to files:
# [corpus_name].br and [corpus_name].en

if [ "$#" -ne 1 ] ; then
  echo "Usage: $0 corpus_name" >&2
  exit 1
fi
corpus=$1

rm "$corpus.en"
rm "$corpus.br"

for file in *.tmx; do
	sed -i -e 's/"en-US"/"en"/g' "$file"
	./tmx2moses.py "$file" en >> "$corpus.en"
	./tmx2moses.py "$file" br >> "$corpus.br"
done
