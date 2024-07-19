FROM python:3.12
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
#RUN python manage.py migrate
EXPOSE 8999


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# 1)build image for dockerfile, через интерфейс
# 2) должен появиться следующий результат :Successfully built 297dfaa1d1b2
                                          #Successfully tagged sweet_friends_image:latest
                                          #'sweet_friends_image Dockerfile: Dockerfile' has been deployed successfully.
# 3) прописать: docker run --name sweet_container -p 8800:8800 sweet_friends_image:latest