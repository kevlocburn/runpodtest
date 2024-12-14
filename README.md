# AI Image Caption Generator + Stable Diffusion

## How to Run


## Local Deployment:

1. git clone https://github.com/kevlocburn/runpodtest.git
   cd runpodtest

2. Create python  environment:
   python -m venv venv
   .\venv\Scripts\activate
3. Install: pip install -r requirements.txt

4. Run: python api.py
   The application will be available at http://127.0.0.1:5000

5. Make a POST request to `/caption` with an image file to get a caption.
   curl -X POST -F "image=@path/to/your/image.jpg" http://127.0.0.1:5000/caption

6. Make a POST request to `/generate` with text to get an image file 
   curl -X POST -H "Content-Type: application/json" -d '{"prompt": "a futuristic cityscape at sunset"}' http://127.0.0.1:5000/generate


## Docker or with runpod.io
1. Build the Docker image:
docker build -t image-caption-generator .

2. Run the container:
   docker run --gpus all -p 5000:5000 image-caption-generator

3. Make a POST request to `/caption` with an image file to get a caption.
   
   curl -X POST -F "image=@path/to/your/image.jpg" http://<POD_IP>:5000/caption


4. Make a POST request to `/generate` with text to get an image file.

   curl -X POST -H "Content-Type: application/json" -d '{"prompt": "a futuristic cityscape at sunset"}' http://<POD_IP>:5000/generate

