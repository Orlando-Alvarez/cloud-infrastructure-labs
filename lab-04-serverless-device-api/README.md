# Lab 04 — Serverless Device API

A serverless REST API built with **AWS Lambda**, **API Gateway**, **DynamoDB**, **IAM**, and **CloudWatch Logs**.

This lab demonstrates how to build a simple cloud-native backend using managed AWS services. The API allows creating, listing, retrieving, and deleting demo device records.

> No real patient, medical, or sensitive data is used in this project.

---

## Architecture

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

## AWS Services Used

- **Amazon API Gateway** — Exposes HTTP endpoints for the API.
- **AWS Lambda** — Runs the backend Python code without managing servers.
- **Amazon DynamoDB** — Stores device records using a NoSQL table.
- **AWS IAM** — Controls Lambda permissions using least privilege.
- **Amazon CloudWatch Logs** — Stores Lambda execution logs for debugging and monitoring.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/devices` | Create a demo device |
| `GET` | `/devices` | List all demo devices |
| `GET` | `/devices/{device_id}` | Retrieve one device by ID |
| `DELETE` | `/devices/{device_id}` | Delete one device by ID |

---

## DynamoDB Table

| Setting | Value |
|---|---|
| Table name | `portfolio-devices` |
| Partition key | `device_id` |
| Key type | String |
| Capacity mode | On-demand |

---

## Lambda Environment Variable

| Key | Value |
|---|---|
| `TABLE_NAME` | `portfolio-devices` |

Using an environment variable avoids hardcoding the DynamoDB table name directly in the source code.

---

## IAM Permissions

The Lambda execution role was granted only the DynamoDB permissions needed for this lab:

```json
{
  "Effect": "Allow",
  "Action": [
    "dynamodb:PutItem",
    "dynamodb:GetItem",
    "dynamodb:Scan",
    "dynamodb:DeleteItem"
  ],
  "Resource": "arn:aws:dynamodb:REGION:ACCOUNT_ID:table/portfolio-devices"
}
```

This follows the principle of least privilege by allowing access only to the required DynamoDB table.

---

## Example Request

PowerShell example using `Invoke-RestMethod`:

```powershell
$BASE_URL="https://your-api-id.execute-api.us-west-2.amazonaws.com"

$body = @{
  device_id = "dev-001"
  device_type = "demo-sensor"
  status = "active"
} | ConvertTo-Json

Invoke-RestMethod -Method Post -Uri "$BASE_URL/devices" -ContentType "application/json" -Body $body
```

---

## Example Response

```json
{
  "message": "Device created",
  "device": {
    "device_id": "dev-001",
    "device_type": "demo-sensor",
    "status": "active",
    "created_at": "2026-04-30T20:44:49+00:00"
  }
}
```

---

## Additional Test Commands

### List all devices

```powershell
Invoke-RestMethod -Method Get -Uri "$BASE_URL/devices" | ConvertTo-Json -Depth 5
```

### Get one device by ID

```powershell
Invoke-RestMethod -Method Get -Uri "$BASE_URL/devices/dev-001" | ConvertTo-Json -Depth 5
```

### Delete one device

```powershell
Invoke-RestMethod -Method Delete -Uri "$BASE_URL/devices/dev-001" | ConvertTo-Json -Depth 5
```

---

## Screenshots

| Screenshot | Description |
|---|---|
| `01-api-gateway-routes.png` | API Gateway routes for `/devices` and `/devices/{device_id}` |
| `02-lambda-overview.png` | Lambda function overview |
| `03-lambda-environment-variable.png` | Lambda environment variable `TABLE_NAME` |
| `04-iam-dynamodb-policy.png` | IAM policy allowing Lambda to access DynamoDB |
| `05-dynamodb-table-item.png` | Item created in DynamoDB by the API |
| `06-post-device-success.png` | Successful `POST /devices` request |
| `07-get-devices-success.png` | Successful `GET /devices` request |
| `08-get-device-by-id-success.png` | Successful `GET /devices/dev-001` request |
| `09-delete-device-success.png` | Successful `DELETE /devices/dev-001` request |
| `10-cloudwatch-logs.png` | CloudWatch Logs showing Lambda execution |

---

## What I Learned

- How to expose a Lambda function using API Gateway HTTP API.
- How API Gateway sends request events to Lambda.
- How to use Python and `boto3` to interact with DynamoDB.
- How to configure Lambda environment variables.
- How to grant Lambda access to DynamoDB using IAM permissions.
- How to validate API behavior using PowerShell and HTTP requests.
- How to inspect Lambda execution using CloudWatch Logs.
- How serverless services can reduce infrastructure management overhead.

---

## Security Notes

- No AWS credentials are hardcoded in the source code.
- The DynamoDB table name is stored as an environment variable.
- The Lambda function uses an IAM execution role.
- DynamoDB permissions are limited to the required table.
- No real medical, patient, or personal data is stored.
- Screenshots should not expose access keys, secret keys, session tokens, or unnecessary account identifiers.

---

## Cost Awareness

This lab uses serverless and on-demand services. For small testing workloads, costs should be minimal, but resources should still be deleted after completing the lab.

Resources to clean up:

1. API Gateway HTTP API
2. Lambda function
3. DynamoDB table
4. IAM role or inline policy created for this lab
5. CloudWatch log group, optional

---

## Project Status

**Status:** Completed

The API was successfully deployed and tested using PowerShell. A device record was created through API Gateway, processed by Lambda, stored in DynamoDB, and verified through CloudWatch Logs.
