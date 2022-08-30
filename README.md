# How to use:
1. Clone the repository 
2. Open the reposity in your terminal and run the followin command:

    <code> docker build --tag flask . </code>

3. Use docker run with the following flags to run the container

    <code>  docker run -d -p 5000:5000 flask </code>

    "-d" to run it in detached mode and 

    "-p" to specify the port to be exposed

    We do that so we can see the application in the browser rather than the container
    
4. Check if docker managed to build the image correctly using

    <code> docker ps </code>

    You should be seeing something like that in your terminal:

    ![image](https://user-images.githubusercontent.com/40416044/187300250-a0b7e4a5-5b49-44b0-a203-9a5062922b3c.png)

5. Go to your <a href="http://localhost:5000/"> localhost </a>  to see the application running with Swagger UI or use another software of your choice, like Postman.

    ![image](https://user-images.githubusercontent.com/40416044/187342589-ac118aba-dba5-49b4-bcc9-d39ee289fdc3.png)

6. Two routes are available: 
    - <code>/encode/:number</code>  - Returns a 6 digit code for the given number (n)
    - <code>/decode/:code</code> - Decodes the given code into a number
