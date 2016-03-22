git init
git remote add origin https://julien_vingtcinq@bitbucket.org/julien_vingtcinq/{{ cookiecutter.project_name }}.git
git add --all
git commit -m"initial commit"
git push --set-upstream origin master

virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

python ./manage.py makemigrations
python ./manage.py migrate

npm install
bower install
