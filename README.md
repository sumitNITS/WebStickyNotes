## A Web Based Sticky Notes 

![sticky notes](https://user-images.githubusercontent.com/37767537/229308712-08a031f1-5670-44b4-875d-ca4b5d37ca6f.png)

### Few features of this project include

- Adding the note ✍️
- ✔️ the note
-  Deleting the note 🗑️

This Sticky Notes app is similar to Windows Sticky Notes App and follows Reverse chronological order. Only exception that once NOTE is added you can't edit it. Alternatively, you can add the NOTE again with latest data and remove the old one.

### Instructions to run this project locally

- Create a project directory called Sticky Notes
- cd to Sticky Notes
- clone this project using the command
```bash
git clone https://github.com/sumitNITS/WebStickyNotes.git
```
- Install virtual environment to run this project locally using the command
```bash
pip install virtualenv
```
- Create a virtual environment for this project using the command
```bash 
python -m virtualenv <name>
```
- Activate the virtual environment to work with this project using the command
```bash
.\<name>\Scripts\activate
```
- cd to WebStickyNotes
- Install python django framework using the command
```bash
pip install django
```
-- Run the below commands
```bash 
python manage.py makemigrations notes
```
```bash 
python manage.py migrate
```
```bash 
python manage.py runserver
```

Now visit the URL http://127.0.0.1:8000/ and explore the application 🚀




