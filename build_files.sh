# build_files.sh
# pip install -r requirements.txt

# make migrations
# python3.12 manage.py migrate 
# python3.12 manage.py collectstatic

build_files.sh

echo " BUILD START"

python3.9 -m pip install -r requirements.txt

python3.9 manage.py collectstatic --noinput --clear

echo " BUILD END"