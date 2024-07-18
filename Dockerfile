# FROM python:3.9-slim

# WORKDIR /app

# COPY . /app

# RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 8000

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



# FROM python:3.9

    
# WORKDIR /app

# COPY . /app
   
# ADD . /app

   
# RUN pip install --no-cache-dir -r requirements.txt

    
# EXPOSE 80

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]




FROM python:3.9

# Set the working directory
WORKDIR /usr/src/app


COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
