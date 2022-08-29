# How to use:
1. Clone the repository 
2. Open the reposity in your terminal and run the followin command:

    <code> docker build --tag flask . </code>

3. Check if docker managed to build the image correctly using

    <code> docker ps </code>

    You should be seeing something like that in your terminal:

    ![image](https://user-images.githubusercontent.com/40416044/187300250-a0b7e4a5-5b49-44b0-a203-9a5062922b3c.png)


4. Use docker run with the following flags to run the container

    <code>  docker run -d -p 5000:5000 flask </code>

    "-d" to run it in detached mode and 

    "-p" to specify the port to be exposed

    We do that so we can see the application in the browser rather than the container

5. Go to your <a href="http://localhost:5000/"> localhost </a>  to see the application running or use another software of your choice to acess the API, like Postman.

6. Two routes are available: 
    - <code>/encode/:number</code>  - which should transform a fixed number into a code with a six character number
    - <code>/decode/:code</code> - which will decode the result of the first route and return the starting number.
