FROM python:3-alpine3.22
LABEL authors="cyneric"

WORKDIR /usr/server
RUN apk update
RUN apk add git cmake sqlite sqlite-dev
# RUN apt-get update && apt-get install git && apt-get install sqlite3
RUN git clone https://github.com/Cyneric400/GardenGuardian.git
WORKDIR /usr/server/GardenGuardian
RUN python -m pip install -r requirements.txt
RUN sqlite3 db/db.db -init VTI64_db/schema.sql ".read db/schema.sql"
WORKDIR /usr/server/DeepNexys-streamlit

CMD ["sh", "-c", "streamlit run app.py"]

EXPOSE 8501
