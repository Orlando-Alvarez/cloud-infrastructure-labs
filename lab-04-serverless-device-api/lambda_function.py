import json
import os
import uuid
from datetime import datetime, timezone

import boto3
from botocore.exceptions import ClientError


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE_NAME"])


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS",
        },
        "body": json.dumps(body),
    }


def parse_body(event):
    try:
        body = event.get("body")

        if not body:
            return {}

        if event.get("isBase64Encoded"):
            return {}

        return json.loads(body)

    except json.JSONDecodeError:
        return None


def create_device(event):
    body = parse_body(event)

    if body is None:
        return response(400, {"error": "Invalid JSON body"})

    device_id = body.get("device_id", f"dev-{uuid.uuid4().hex[:8]}")
    device_type = body.get("device_type", "demo-device")
    status = body.get("status", "active")

    item = {
        "device_id": device_id,
        "device_type": device_type,
        "status": status,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    table.put_item(Item=item)

    return response(201, {
        "message": "Device created",
        "device": item
    })


def list_devices():
    result = table.scan()
    items = result.get("Items", [])

    return response(200, {
        "count": len(items),
        "devices": items
    })


def get_device(event):
    path_params = event.get("pathParameters") or {}
    device_id = path_params.get("device_id")

    if not device_id:
        return response(400, {"error": "device_id is required"})

    result = table.get_item(Key={"device_id": device_id})
    item = result.get("Item")

    if not item:
        return response(404, {"error": "Device not found"})

    return response(200, item)


def delete_device(event):
    path_params = event.get("pathParameters") or {}
    device_id = path_params.get("device_id")

    if not device_id:
        return response(400, {"error": "device_id is required"})

    table.delete_item(Key={"device_id": device_id})

    return response(200, {
        "message": "Device deleted",
        "device_id": device_id
    })


def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    route_key = event.get("routeKey")

    try:
        if route_key == "POST /devices":
            return create_device(event)

        if route_key == "GET /devices":
            return list_devices()

        if route_key == "GET /devices/{device_id}":
            return get_device(event)

        if route_key == "DELETE /devices/{device_id}":
            return delete_device(event)

        if event.get("requestContext", {}).get("http", {}).get("method") == "OPTIONS":
            return response(200, {"message": "CORS preflight OK"})

        return response(404, {
            "error": "Route not found",
            "routeKey": route_key
        })

    except ClientError as error:
        print("AWS ClientError:", str(error))
        return response(500, {
            "error": "AWS service error",
            "details": str(error)
        })

    except Exception as error:
        print("Unexpected error:", str(error))
        return response(500, {
            "error": "Internal server error",
            "details": str(error)
        })
