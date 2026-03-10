import json

# Step 1: Store the JSON-formatted API response as a string
api_response = '''
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''

# Step 2: Parse the JSON string into a Python dictionary
response_data = json.loads(api_response)

# Step 3: Extract required values
request_id = response_data["id"]
status = response_data["status"]
text_result = response_data["result"]["text"]
confidence_score = response_data["result"]["confidence"]

# Step 4: Print extracted values
print("Request ID:", request_id)
print("Status:", status)
print("Text:", text_result)
print("Confidence:", confidence_score)

# Step 5: Check confidence threshold
if confidence_score < 0.9:
    print("Warning: Confidence score is below acceptable threshold!")

# Step 6: Create a new Python dictionary for follow-up result
follow_up_result = {
    "request_id": request_id,
    "processed": True,
    "message": "Response processed successfully"
}

# Step 7: Convert dictionary to JSON string
follow_up_json = json.dumps(follow_up_result, indent=4)

# Step 8: Write JSON output to a file
with open("response.json", "w") as file:
    file.write(follow_up_json)

print("\nFollow-up JSON written to response.json")
