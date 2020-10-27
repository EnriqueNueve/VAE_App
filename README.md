# VAE_App
A small demo app for a VAE trained to reconstruct face images.

## To Use 
1. Follow link and download model: https://drive.google.com/file/d/1e3rw8GIkOYnuORjZ2MDRC9Kbi98oEHud/view?usp=sharing
2. Place model in main dir of app

3. Follow commands below 
```
# Build docker image
docker build -t vae_app .
# Run docker image
docker run -p 8501:8501 vae_app
# View app by entering url into browser
http://localhost:8501/
# Close docker instance 
ctrl-d
```
