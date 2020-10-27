# docker build -t vae_app .
# docker run -it --memory="8g" --memory-swap="8g" -p 8501:8501 vae_app
# docker run -p 8501:8501 vae_app
# http://localhost:8501/

FROM python:3.7

# streamlit-specific commands
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /root/.streamlit/config.toml'

# exposing default port for streamlit
EXPOSE 8501

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY vae_app.py ./
COPY 36.jpg ./
COPY 57.jpg ./
COPY decoder_lite.tflite ./



CMD ["streamlit","run","./vae_app.py"]
