install npm if it does not exist, then

npm install @apidevtools/swagger-parser

**Converts Swagger 2.0 or OpenAPI >=3.0 file to a list of apis.
Structure of the api:

The structure includes "name", "request", and "response".
The "request" field includes:
"method": the HTTP method (GET, POST, etc.).
"header": headers extracted from the parameters in the spec.
"body": body data extracted from the request body.
"url": URL path, formatted with baseUrl.
"description": description of the API.
The "response" field includes the status, description, and body of the response.
