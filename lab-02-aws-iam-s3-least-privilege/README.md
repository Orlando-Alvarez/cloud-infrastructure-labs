# Lab 02 – AWS IAM Least Privilege Access to S3

## Objective

The goal of this lab was to practice AWS IAM fundamentals by implementing a least-privilege access model for an Amazon S3 bucket.

In this lab, I created an IAM user that can read files only from a specific S3 prefix named `reports/`. The user cannot read private files, upload objects, delete objects, or modify bucket permissions.

I also created an IAM role for EC2 and added a bucket policy that denies insecure non-HTTPS requests.

---

## AWS Services Used

- AWS IAM
- Amazon S3
- IAM Users
- IAM Groups
- IAM Policies
- IAM Roles
- S3 Bucket Policies

---

## Architecture Overview

```text
IAM User: lab2-auditor
        |
        v
IAM Group: Lab2Auditors
        |
        v
IAM Policy: S3 reports read-only access
        |
        v
S3 Bucket
├── reports/
│   └── readme.txt      Allowed
└── private/
    └── secrets.txt     Denied
```

EC2 role concept:

```text
EC2 Instance
        |
        v
IAM Role: EC2 S3 read-only role
        |
        v
IAM Policy: S3 reports read-only access
```

---

## What I Built

### 1. Private S3 Bucket

I created a private Amazon S3 bucket with:

- Block Public Access enabled
- ACLs disabled
- Server-side encryption enabled with SSE-S3
- Two prefixes: `reports/` and `private/`

Test objects:

```text
reports/readme.txt
private/secrets.txt
```

---

### 2. Custom IAM Policy

I created a custom IAM policy that allows the minimum permissions required for the auditor user.

The policy allows:

- Listing buckets in the S3 console
- Listing the specific S3 bucket
- Reading objects only inside `reports/`

The policy does not allow:

- Reading objects inside `private/`
- Uploading objects
- Deleting objects
- Modifying bucket permissions

Example policy with account-specific details redacted:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ConsoleListBuckets",
      "Effect": "Allow",
      "Action": "s3:ListAllMyBuckets",
      "Resource": "*"
    },
    {
      "Sid": "AllowBucketLocationAndList",
      "Effect": "Allow",
      "Action": [
        "s3:GetBucketLocation",
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::lab5-iam-orlando-usw2-ACCOUNT-ID-us-west-2-an"
    },
    {
      "Sid": "AllowReadOnlyReportsFolder",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::lab5-iam-orlando-usw2-ACCOUNT-ID-us-west-2-an/reports/*"
    }
  ]
}
```

---

### 3. IAM Group

I created an IAM group for auditor-style access.

```text
Lab2Auditors
```

The custom S3 read-only policy was attached to this group.

Using a group makes permission management cleaner because additional auditor users can receive the same access by being added to the group.

---

### 4. IAM User

I created an IAM user for testing.

```text
lab2-auditor
```

The user was added to the `Lab2Auditors` group and tested from the AWS Management Console.

---

## Permission Tests

| Test | Expected Result | Actual Result |
|---|---|---|
| Open `reports/readme.txt` | Allowed | Passed |
| Open `private/secrets.txt` | Access Denied | Passed |
| Upload a new file | Access Denied | Passed |
| Delete `reports/readme.txt` | Access Denied | Passed |

---

## IAM Role for EC2

I created an IAM role for EC2 so an EC2 instance could access S3 without storing long-term access keys on the server.

The role trust policy allows EC2 to assume the role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Key concept:

```text
Trust policy = who can assume the role
Permissions policy = what the role can do
```

This avoids storing permanent IAM access keys inside an EC2 instance.

---

## S3 Bucket Policy

I added a bucket policy to deny insecure HTTP requests and require secure transport.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyInsecureTransport",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::lab5-iam-orlando-usw2-ACCOUNT-ID-us-west-2-an",
        "arn:aws:s3:::lab5-iam-orlando-usw2-ACCOUNT-ID-us-west-2-an/*"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
```

This is a resource-based policy because it is attached directly to the S3 bucket.

---

## Key Concepts Learned

### Least Privilege

The IAM user received only the permissions needed to read files from `reports/`.

The user could not upload, delete, or access private files.

### Implicit Deny

The user was denied access to `private/secrets.txt` because there was no explicit `Allow` for that object.

In IAM, if an action is not explicitly allowed, it is denied by default.

### Explicit Deny

The bucket policy included an explicit deny for non-HTTPS requests.

Explicit deny always overrides allow.

```text
Explicit Deny > Allow > Implicit Deny
```

### Identity-Based Policy vs Resource-Based Policy

Identity-based policy:

```text
Policy attached to an IAM user, group, or role
```

Resource-based policy:

```text
Policy attached directly to an AWS resource
```

### IAM Role for AWS Services

An IAM role allows AWS services like EC2 to receive temporary credentials.

This is safer than storing long-term access keys inside servers or applications.

---

## Screenshots

> Screenshots should not expose passwords, access keys, or full sensitive account information.

| Screenshot | Description |
|---|---|
| `01-s3-bucket-folders.png` | S3 bucket with `reports/` and `private/` prefixes |
| `02-iam-policy-json.png` | Custom IAM policy JSON |
| `03-iam-group-policy.png` | IAM group with policy attached |
| `04-iam-user-group.png` | IAM user added to group |
| `05-reports-access-success.png` | Successful access to `reports/readme.txt` |
| `06-private-access-denied.png` | Access denied to `private/secrets.txt` |
| `07-upload-access-denied.png` | Upload denied |
| `08-delete-access-denied.png` | Delete denied |
| `09-ec2-role-trust-policy.png` | EC2 IAM role trust relationship |
| `10-bucket-policy-secure-transport.png` | S3 bucket policy enforcing HTTPS |

---

## Cleanup

To avoid leaving unused resources, the following resources should be deleted after testing:

- IAM user
- IAM group
- IAM role
- Custom IAM policy
- S3 objects
- S3 bucket

---

## What This Lab Demonstrates

This lab demonstrates practical knowledge of:

- IAM users, groups, policies, and roles
- Least privilege access design
- S3 bucket permissions
- Identity-based policies
- Resource-based policies
- Explicit deny and implicit deny
- Secure access to AWS services using IAM roles
- Avoiding long-term access keys on EC2 instances
