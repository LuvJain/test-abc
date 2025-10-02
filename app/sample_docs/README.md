# Sample Documents Directory

This directory contains sample PDF documents for testing the document parsing functionality.

Sample documents are either provided by the user or generated dynamically when requested through the API.

## API Endpoints

You can use the sample document feature through the following API endpoint:

```
POST /documents/sample
```

With the following JSON body:
```json
{
  "sample_name": "sample1.pdf"
}
```

This will create a sample document with the specified name if it doesn't exist, or use the existing sample document if it's already present.