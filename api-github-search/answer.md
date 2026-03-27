# API Explanation

## 1. Role of Query Parameters

Query parameters are used to control what kind of data we want from the API.

In this request, they help in:
- Filtering results using the keyword "python"
- Sorting repositories based on the number of stars
- Setting the order to descending so that the most popular repositories appear first
- Limiting the number of results returned (only top 5)

Without query parameters, the API would return either default results or too much data, which may not be useful.

---

## 2. Why use response.json() instead of response.text?

The GitHub API returns data in JSON format, which is structured like a dictionary in Python.

Using `response.json()`:
- Converts the API response directly into a Python dictionary
- Makes it easy to access specific fields like repository name or stars

If we use `response.text`:
- The output will be a plain string
- We would need to manually parse it, which is more complicated

So, `response.json()` is more convenient and efficient for working with API data.