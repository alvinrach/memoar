FROM python:3.11

WORKDIR /usr/src/app

# install
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy source assets
COPY main.py ./
COPY pytest.py ./

# # Expose the port that Streamlit will run on 
# # this actually dont needed but for documentation
# EXPOSE 8000