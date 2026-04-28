# Cloud Infrastructure Labs

This repository contains hands-on cloud infrastructure labs focused on Azure, AWS concepts, Linux, networking, web servers, and DevOps fundamentals.

The goal of this repository is to document practical cloud labs in a clear and professional way, showing the architecture, commands used, troubleshooting steps, screenshots, and lessons learned.

## Labs

| Lab | Topic | Cloud Provider | Status |
|---|---|---|---|
| [Lab 01](lab-01-azure-vm-nginx/) | Linux VM with NGINX Web Server | Azure | Completed |
| [Lab 05](lab-02-aws-iam-s3-least-privilege/) | IAM Least Privilege Access to S3 | AWS | Completed |

## Skills Practiced

- Linux server administration
- SSH access with private keys
- Public and private IP addressing
- Network Security Groups and firewall rules
- Web server deployment with NGINX
- Cloud compute fundamentals
- Basic cloud troubleshooting
- Mapping Azure services to AWS equivalents
- AWS IAM users, groups, policies, and roles
- Least privilege access design
- Amazon S3 bucket permissions
- Identity-based policies and resource-based policies
- IAM role trust relationships
- Explicit deny and implicit deny

## Repository Structure

```text
```text
cloud-infrastructure-labs/
├── README.md
├── .gitignore
├── lab-01-azure-vm-nginx/
│   ├── README.md
│   ├── index.html
│   └── screenshots/
│       ├── azure-vm-overview.png
│       ├── nsg-rules.png
│       ├── nginx-status.png
│       ├── curl-localhost.png
│       └── browser-test.png
└── lab-02-aws-iam-s3-least-privilege/
    ├── README.md
    └── screenshots/
        ├── 01-s3-bucket-folders.png
        ├── 02-iam-policy-json.png
        ├── 03-iam-group-policy.png
        ├── 04-iam-user-group.png
        ├── 05-reports-access-success.png
        ├── 06-private-access-denied.png
        ├── 07-upload-access-denied.png
        ├── 08-delete-access-denied.png
        ├── 09-ec2-role-trust-policy.png
        └── 10-bucket-policy-secure-transport.png
```

## Purpose

These labs are part of my cloud engineering learning path and are designed to build practical experience with real cloud infrastructure scenarios.

