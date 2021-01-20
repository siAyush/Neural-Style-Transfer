# Neural Style Transfer

Neural style transfer consists in generating an image with the same "content" as a base image, but with the "style" of a different picture. 
This is achieved through the optimization of a loss function that has 3 components: "style loss", "content loss", and "total variation loss".



## Implementation Details
This implementation uses TensorFlow2.x to train a fast style transfer network and Flask as an backend API.


## How to Run?
Requirements:
1. Flask
2. Tensorflow 2.x

```
python3 app.py
```

## Example
Base Image 

![Base](static/images/20b76145-957a-4547-aa24-0f10733bc96f.png)

Style Image

![Style](static/images/978dbb85-25c2-4074-ac59-78caa2a1d694.png)


Genrated Image

![Genrated](genrated.png)
