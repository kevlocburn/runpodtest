# AI Image Caption Generator

## How to Run

1. Build the Docker image:
docker build -t image-caption-generator .

2. Run the container:
docker run --gpus all -p 5000:5000 image-caption-generator


3. Make a POST request to `/caption` with an image file to get a caption.
