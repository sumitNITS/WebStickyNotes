## A Web-Based Sticky Notes 

![sticky notes](https://user-images.githubusercontent.com/37767537/229308712-08a031f1-5670-44b4-875d-ca4b5d37ca6f.png)

### A Few features of this project include

- Adding the note ✍️
- ✔️ the note
-  Deleting the note 🗑️

This Sticky Notes app is similar to Windows Sticky Notes App and follows Reverse chronological order for taking notes. The only exception is that once NOTE is added you can't edit it. Alternatively, you can add the NOTE again with your latest data and remove the old one.

### Instructions to run this project locally

- Create a project directory called Sticky Notes
- cd to Sticky Notes
- Clone this project using the command
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
- Run the below commands
```bash 
python manage.py makemigrations notes
```
```bash 
python manage.py migrate
```
```bash 
python manage.py runserver
```

Now visit the URL http://127.0.0.1:8000/ and explore the Sticky Notes application 🚀

### Instructions to run this project as Docker container

- cd to WebStickyNotes
- Build an image out of Dockerfile using the command 
```bash
docker build . -t <image-name>
```
- Start the container with the docker image using the command
```bash
docker run -d -p <port>:8000 --name stickynotes <image-name> 
```
Now access the Sticky Notes application using "localhost":"port" OR "ip-of-machine":"port" 🚀

### Instructions to run this project using dockerhub image

- Access the Sticky Notes application using the command 
```bash
docker run -d -p <port>:8000 --name stickynotes sumit0058/stickynotes:1.0
```







