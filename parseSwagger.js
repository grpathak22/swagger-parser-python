const fs = require("fs");
const SwaggerParser = require("@apidevtools/swagger-parser");

async function parseSwagger(filePath) {
  try {
    const api = await SwaggerParser.dereference(filePath);
    console.log(JSON.stringify(api, null, 2)); // Output parsed API as JSON
  } catch (error) {
    console.error("Error parsing Swagger:", error.message);
  }
}

// Get file path from command-line arguments
const filePath = process.argv[2];
if (!filePath) {
  console.error("Usage: node parseSwagger.js <path_to_swagger_file>");
  process.exit(1);
}

parseSwagger(filePath);
