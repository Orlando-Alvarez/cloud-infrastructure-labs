# Cloud Engineering Portfolio

This repository contains hands-on cloud engineering labs focused on **AWS**, **Azure**, Linux, security, serverless architecture, and cloud operations.

The goal of this portfolio is to demonstrate practical cloud skills through real deployments, documented configurations, screenshots, cleanup steps, and lessons learned.

---

## About This Portfolio

This portfolio is being built as part of my preparation for cloud engineering, cloud development, and DevOps-focused roles.

The labs are designed to show practical experience with:

- Cloud infrastructure
- Identity and access management
- Secure data handling
- Serverless APIs
- Linux administration
- Networking basics
- Monitoring and logs
- Cost-aware resource cleanup
- Portfolio-quality technical documentation

---

## Labs

| Lab | Topic | Cloud Provider | Status |
|---|---|---|---|
| [Lab 01](lab-01-linux-vm-nginx-web-server/) | Linux VM with NGINX Web Server | Azure | Completed |
| [Lab 02](labs/lab-02-iam-least-privilege-s3/) | IAM Least Privilege Access to S3 | AWS | Completed |
| [Lab 03](labs/lab-03-kms-secrets-manager-secure-data-controls/) | KMS, Secrets Manager, and Secure Data Controls | AWS | Completed |
| [Lab 04](labs/lab-04-serverless-device-api/) | Serverless REST API with Lambda, API Gateway, and DynamoDB | AWS | Completed |

> If your local folder names are different, update the links in the table to match your actual repository structure.

---

## Lab Summaries

### Lab 01 — Linux VM with NGINX Web Server

**Cloud Provider:** Azure  
**Main Focus:** Linux, virtual machines, web servers, networking, inbound rules

In this lab, I deployed a Linux virtual machine, installed and configured NGINX, opened the required inbound network ports, and verified access to the web server from a browser and terminal.

**Skills practiced:**

- Linux VM deployment
- NGINX installation
- Network security rules
- Public IP access
- HTTP traffic validation
- Basic cloud troubleshooting

---

### Lab 02 — IAM Least Privilege Access to S3

**Cloud Provider:** AWS  
**Main Focus:** IAM, S3, access control, least privilege

In this lab, I practiced controlling access to Amazon S3 using IAM users, groups, policies, and least-privilege permissions.

**Skills practiced:**

- IAM users and groups
- AWS managed vs custom policies
- S3 bucket access
- Least-privilege access design
- Permission testing
- AWS CLI usage

---

### Lab 03 — KMS, Secrets Manager, and Secure Data Controls

**Cloud Provider:** AWS  
**Main Focus:** Encryption, secrets management, secure data handling

In this lab, I explored AWS security services used to protect sensitive data, including AWS KMS and AWS Secrets Manager.

**Skills practiced:**

- AWS KMS key concepts
- Encryption at rest
- Encryption in transit concepts
- Secrets Manager
- Secret rotation concepts
- Secure configuration practices
- IAM access to encrypted resources

---

### Lab 04 — Serverless Device API

**Cloud Provider:** AWS  
**Main Focus:** Serverless development, REST APIs, Lambda, DynamoDB, CloudWatch

In this lab, I built a serverless REST API using API Gateway, AWS Lambda, DynamoDB, IAM, and CloudWatch Logs. The API can create, list, retrieve, and delete demo device records.

**Architecture:**

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

**Skills practiced:**

- API Gateway HTTP API routes
- AWS Lambda with Python
- DynamoDB table design
- IAM execution role permissions
- Environment variables
- CloudWatch Logs troubleshooting
- REST API testing with PowerShell
- Serverless cost awareness

---

## Skills Practiced

### Cloud Platforms

- AWS
- Azure

### Compute

- Azure Virtual Machines
- AWS Lambda

### Storage and Databases

- Amazon S3
- Amazon DynamoDB

### Security

- AWS IAM
- Least privilege permissions
- AWS KMS
- AWS Secrets Manager
- Resource policies
- Environment variables
- Secure data handling concepts

### Networking

- HTTP access
- Inbound rules
- Public IP access
- API Gateway endpoints
- Basic cloud connectivity testing

### Monitoring and Troubleshooting

- CloudWatch Logs
- Terminal-based testing
- PowerShell HTTP requests
- Endpoint validation
- Error diagnosis

### Development and Operations

- Python
- REST API concepts
- JSON
- PowerShell
- Linux CLI
- GitHub documentation
- Resource cleanup and cost control

---

## Security Practices Followed

Across these labs, I focused on basic but important cloud security practices:

- Avoiding hardcoded credentials
- Using IAM roles and policies
- Applying least-privilege permissions
- Avoiding real personal, patient, or sensitive data
- Using environment variables for configuration
- Documenting cleanup steps
- Reviewing what information appears in screenshots before publishing

---

## Cost Awareness

These labs are designed to be small and cost-aware. Resources should be deleted after testing unless they are intentionally kept for demonstration.

Typical cleanup includes:

- Deleting test APIs
- Deleting Lambda functions
- Deleting unused DynamoDB tables
- Removing unnecessary IAM roles or policies
- Deleting CloudWatch log groups when no longer needed
- Stopping or deleting cloud virtual machines
- Removing unused public IPs or related networking resources

---

## Portfolio Purpose

This repository demonstrates hands-on learning and practical cloud implementation.

It is intended to support applications for roles such as:

- Cloud Engineer
- Associate Cloud Engineer
- Cloud Developer
- Junior DevOps Engineer
- Infrastructure / Platform Engineering Intern or Entry-Level Role
- Software Engineer with cloud-focused responsibilities

---

## Current Status

The portfolio is actively being expanded.

Completed labs currently cover:

- Linux VM deployment
- NGINX web server setup
- AWS IAM and S3 permissions
- AWS encryption and secrets management
- Serverless API development with Lambda, API Gateway, and DynamoDB

Planned future areas include:

- Application Load Balancer
- Auto Scaling Groups
- VPC public and private subnets
- RDS in private subnets
- NAT Gateway
- VPC endpoints
- Route 53
- HTTPS with ACM
- Docker deployments
- Terraform infrastructure as code
- CI/CD with GitHub Actions
- CloudWatch alarms and SNS notifications
- Disaster recovery architecture

---

## Notes

All labs are for educational and portfolio purposes.

No production workloads, real customer data, medical data, personal data, or sensitive credentials are used.
