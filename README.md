shop_curd
================
shop_curd is a curd (suprise) written in python django (django-rest-framework). I wanted to have at least one project "made as it should be made", so let's say it's my project for CV.
![image](https://user-images.githubusercontent.com/64653975/183323628-131158f7-a397-4571-b263-fb4667f915c8.png)


# Schema
![](![schema](https://user-images.githubusercontent.com/64653975/183323952-04297e1c-b06b-44fc-b50c-b6baf2fccd29.png))

This is really the first time when I've used knowledge from my school in "real work". Project database schema is based on assigment which I got on my databases classes (so you can see db visualisation from MS Access above). I tried to be as accurate as I could/it was possible. 

Database is made for some sort of book shop. (Unfortunately) schema and whole assigment was in polish and that's why i have written some objects in that language. I know it looks awful (especially when you understand this language) but I really wanted to transfer database from scratch to Django-ORM.

# how to run?
```bash
git clone https://github.com/RandomGuy090/shop_curd
cd shop_curd

pip3 install -r requirements.txt
python3 manage.py startserver

```

or if you prefer to user docker: 
```bash
git clone https://github.com/RandomGuy090/shop_curd
cd shop_curd

docker build --tag shop_curd .
docker run -d -p 8000:8000 shop_curd
# go to http://127.0.0.1:8000 

```