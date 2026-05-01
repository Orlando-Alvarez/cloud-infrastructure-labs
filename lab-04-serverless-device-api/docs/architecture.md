# Architecture — Serverless Device API

## Overview

This lab implements a small serverless REST API using AWS managed services.

The API receives HTTP requests through Amazon API Gateway, invokes an AWS Lambda function written in Python, and stores demo device records in Amazon DynamoDB. Lambda execution logs are stored in Amazon CloudWatch Logs.

No real patient, medical, personal, or sensitive data is used.

---

## Architecture Diagram

```text
Client / PowerShell / curl
        |
        v
Amazon API Gateway HTTP API
        |
        v
AWS Lambda Python Function
        |
        v
Amazon DynamoDB
        |
        v
Amazon CloudWatch Logs
```

---

## Request Flow

1. A client sends an HTTP request to the API Gateway endpoint.
2. API Gateway matches the request to one of the configured routes.
3. API Gateway invokes the `device-api-lambda` function.
4. Lambda reads the route key and decides which function to run.
5. Lambda uses `boto3` to interact with the `portfolio-devices` DynamoDB table.
6. Lambda returns a JSON response to API Gateway.
7. API Gateway returns the HTTP response to the client.
8. Lambda logs are stored in CloudWatch Logs.

---

## Routes

| Method | Path | Lambda Action |
|---|---|---|
| POST | `/devices` | Create a demo device |
| GET | `/devices` | List all demo devices |
| GET | `/devices/{device_id}` | Get one device by ID |
| DELETE | `/devices/{device_id}` | Delete one device by ID |

---

## AWS Components

### Amazon API Gateway

Used as the public HTTP entry point for the API.

### AWS Lambda

Runs the backend Python code without requiring a server.

### Amazon DynamoDB

Stores demo device records. The table uses `device_id` as the partition key.

### AWS IAM

The Lambda execution role grants only the permissions required to access the DynamoDB table.

### Amazon CloudWatch Logs

Stores Lambda logs, including request events and execution reports.

---

## Security Considerations

- No AWS credentials are stored in the code.
- The DynamoDB table name is stored as a Lambda environment variable.
- The Lambda execution role follows least-privilege access for this lab.
- No sensitive or real-world medical data is used.
- Screenshots should not expose access keys, secret keys, session tokens, or unnecessary account identifiers.

---

## Cost Considerations

This lab uses serverless and on-demand resources. Costs should be minimal for small tests, but resources should be deleted after the lab is completed.

Resources to clean up:

1. API Gateway HTTP API
2. Lambda function
3. DynamoDB table
4. IAM role or inline policy created for the lab
5. CloudWatch log group, optional
