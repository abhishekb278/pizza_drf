--------------------------------------------TO RUN PROJECT--------------------------------------------------
====OPEN CMD====
_______________________________
install MongoDB : https://www.mongodb.com/try/download/community?tck=docs_server
create a database in mongodb and name it as :- mypizza
pip install -r requirements.txt
_______________________________

python manage.py makemigrations
python manage.py migrate
python manage.py runserver



________________________________________________________________________________________________________________
After python manage.py runserver
Go to these urls in chrome
________________________

	API endpoint to create regular pizza and a square pizza 
	http://127.0.0.1:8000/pizza/

        Lists the information about all the stored pizza
	http://127.0.0.1:8000/listpizza/

	Filtering the list of pizza returned by the API based on Size & Type of Pizza
	http://127.0.0.1:8000/listpizza/?types=Regular&sizes=2

	API endpoint that allows the user to edit or delete any pizza
	http://127.0.0.1:8000/modpizza/1/


