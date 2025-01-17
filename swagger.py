import subprocess
import json
import os

class SwaggerParser:
    def __init__(self, node_script_path="parseSwagger.js"):
        self.node_script_path = node_script_path

    def parse_swagger(self, swagger_file_path):
        """
        Parse a Swagger file using the Node.js script and return the parsed JSON.
        """
        try:
            # Call the Node.js script
            result = subprocess.run(
                ["node", self.node_script_path, swagger_file_path],
                capture_output=True,
                text=True,
                check=True
            )
            # Parse the JSON output
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error running Node.js script: {e.stderr}")
            return None

    def extract_requests(self, parsed_spec):
        """
        Transform the parsed Swagger spec into the desired request array format.
        """
        requests = []
        paths = parsed_spec.get("paths", {})

        for path, methods in paths.items():
            for method, details in methods.items():
                # Extract request details
                name = details.get("summary", details.get("operationId", "Unnamed API"))
                description = details.get("description", "")
                parameters = details.get("parameters", [])
                request_body = details.get("requestBody", {})
                responses = details.get("responses", {})

                # Prepare headers and request body
                headers = {}
                for param in parameters:
                    if param.get("in") == "header":
                        headers[param["name"]] = f"<{param.get('schema', {}).get('type', 'string')}>"

                body = {}
                if "content" in request_body:
                    content = request_body["content"].get("application/json", {})
                    body = content.get("example", content.get("schema", {}))

                # Transform responses
                response_data = []
                for status, response_details in responses.items():
                    response_body = {}
                    if "content" in response_details:
                        content = response_details["content"].get("application/json", {})
                        response_body = content.get("example", content.get("schema", {}))

                    response_data.append({
                        "status": status,
                        "description": response_details.get("description", ""),
                        "body": response_body
                    })

                # Add to request array in the required format
                requests.append({
                    "name": name,
                    "request": {
                        "method": method.upper(),
                        "header": headers,
                        "body": body,
                        "url": f"{{baseUrl}}{path}",
                        "description": description
                    },
                    "response": response_data
                })

        return requests


# swagger_file = ""  # Replace with your Swagger file path
# parser = SwaggerParser()
# parsed_data = parser.parse_swagger(swagger_file)
# # print(parsed_data)
# requests_array = parser.extract_requests(parsed_data)
