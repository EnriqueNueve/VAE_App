# VAE_App
A small demo app for a VAE trained to reconstruct face images.

## To Use 
```
# Build docker image
docker build -t vae_app .
# Run docker image
docker run -p 8501:8501 vae_app
# View app in browser
http://localhost:8501/
# Close docker instance 
ctrl-d
```
