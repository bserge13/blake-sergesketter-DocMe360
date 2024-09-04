FROM python:3-alpine3.15
# WORKDIR /app
# COPY . /app
# RUN pip install -r requirements.txt
# EXPOSE 5000
# # CMD python ./create_db.py
# CMD python ./api.py

# terminal command: docker build -t chickpea/docme360 .
# docker container run -d -p 5000:3000 chickpea/docme360 
# docker container ls (confirm the long string return from run to what's in ls)
# docker container stop ### (first three digits of our docker container)
# docker push chickpea/docme360