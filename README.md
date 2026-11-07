# number_web_service
Simple Docker deployed API on AWS ECS that can accept numbers and convert them to text. First shot for 1 to 10.

1. First, run **docker images** locally to see list of all the images present locally in Docker Desktop.
2. Execute **docker build -t number-web-service-v00 .** to create a local Docker image that has this web service.
3. -t lists a tag but since we did not provide any tags, it automatically suffixes :latest to the image name.
4. **docker run -p 5001:5001 -e APP_API_KEY=password1 number-web-service-v00** will execute this for client calls
5. Open another Mac OS X Terminal
6. Execute this command to get **curl** talking to the Docker service
7. **curl -i -X POST http://127.0.0.1:5001/convert \
     -H "Content-Type: application/json" \
     -H "X-API-Key: password1" \
     -d '{"number": 10}'**
8. You should see this output:
**HTTP/1.1 200 OK
Server: gunicorn
Date: Sat, 07 Nov 2026 22:11:01 GMT
Connection: close
Content-Type: application/json
Content-Length: 34

{"converted":"ten","original":10}**
