# Cloud Infrastructure Labs

This repository contains hands-on cloud infrastructure labs focused on Azure, AWS, Linux, networking, security, web servers, and DevOps fundamentals.

The goal of this repository is to document practical cloud labs in a clear and professional way, showing the architecture, steps performed, IAM policies, troubleshooting notes, screenshots, and lessons learned.

## Labs

| Lab | Topic | Cloud Provider | Status |
|---|---|---|---|
| [Lab 01](lab-01-azure-vm-nginx/) | Linux VM with NGINX Web Server | Azure | Completed |
| [Lab 02](lab-02-aws-iam-s3-least-privilege/) | IAM Least Privilege Access to S3 | AWS | Completed |
| [Lab 03](lab-03-kms-secrets-manager/) | KMS, Secrets Manager, and Secure Data Controls | AWS | Completed |

## Skills Practiced

- Linux server administration
- SSH access with private keys
- Public and private IP addressing
- Network Security Groups and firewall rules
- Web server deployment with NGINX
- Amazon S3 bucket configuration
- IAM users, groups, roles, and policies
- Least-privilege access design
- S3 bucket policies
- Server-side encryption
- AWS KMS customer managed keys
- SSE-KMS encrypted S3 objects
- AWS Secrets Manager
- Secure handling of fake credentials
- AccessDenied troubleshooting
- Basic cloud security documentation
- Mapping Azure services to AWS equivalents

## Repository Structure

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
├── lab-02-aws-iam-s3-least-privilege/
│   ├── README.md
│   └── screenshots/
└── lab-03-kms-secrets-manager/
    ├── README.md
    ├── screenshots/
    │   ├── 01-kms-key-created.png
    │   ├── 02-s3-object-sse-kms.png
    │   ├── 03-s3-access-denied-kms-decrypt.png
    │   ├── 04-s3-access-success-after-kms-decrypt.png
    │   ├── 05-secrets-manager-access-denied.png
    │   └── 06-secret-value-access-success.png
    └── iam-policies/
        ├── s3-read-without-kms.json
        ├── kms-decrypt.json
        ├── secrets-metadata-only.json
        └── secrets-read-value.json
```

## Purpose

These labs are part of my cloud engineering learning path and are designed to build practical experience with real cloud infrastructure scenarios.

Each lab focuses on understanding how cloud services work in practice, how permissions affect access, how to troubleshoot common issues, and how to document technical work clearly for a professional portfolio.

## Notes

All sensitive information such as account IDs, ARNs, request IDs, host IDs, and credentials is redacted from screenshots and code examples.

Any credentials shown in the labs are fake and used only for demonstration purposes.
