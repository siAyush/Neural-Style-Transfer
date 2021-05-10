<H1> <div align="center"> Neural Style Transfer </H1>
<br>

<p align="center">
    <img alt="Python" src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>
    <img alt="NumPy" src="https://img.shields.io/badge/numpy%20-%23013243.svg?&style=for-the-badge&logo=numpy&logoColor=white" />
    <img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow%20-%23FF6F00.svg?&style=for-the-badge&logo=TensorFlow&logoColor=white" />
    <img alt="Jupyter" src="https://img.shields.io/badge/Jupyter%20-%23F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white" />
</p>
<br>
<div align="center"> 
Neural style transfer consists in generating an image with the same "content" as a base image, but with the "style" of a different picture. 
This is achieved through the optimization of a loss function that has 3 components: "style loss", "content loss", and "total variation loss".
</div>


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

<div align="center"> 
    
![Base](static/images/20b76145-957a-4547-aa24-0f10733bc96f.png)

</div>

Style Image

<div align="center"> 
    
![Style](static/images/978dbb85-25c2-4074-ac59-78caa2a1d694.png)

</div>

Genrated Image
<div align="center"> 
    
![Genrated](genrated.png)

</div>
