# AWS DevSecOps Project 1 – Secure CI/CD Pipeline for Containerized Flask App

## Overview

This project demonstrates a practical DevSecOps workflow on AWS, where a containerized Python (Flask) application is built, stored, deployed, and monitored using AWS-native services.

The goal is to simulate a real-world cloud deployment pipeline with integrated security practices, evolving from a simple local container setup to a production-like architecture.

---

## Current Architecture

Local Flask App → Docker Image → Amazon ECR → Amazon ECS Fargate → CloudWatch Logs

---

## Target Architecture (Planned)

GitHub → CodePipeline → CodeBuild → ECR → ECS Fargate → ALB → CloudWatch

---

## Services Used (Current)

* Amazon ECS (Fargate)
* Amazon ECR
* Amazon CloudWatch
* AWS IAM
* Amazon VPC (default)

---

## Services Planned

* AWS CodePipeline
* AWS CodeBuild
* AWS Secrets Manager
* Terraform

---

## Features

* Containerized Flask application using Docker
* Image storage in Amazon ECR with scan-on-push enabled
* Deployment on ECS Fargate (serverless containers)
* Centralized logging using CloudWatch
* Environment variables injected into containers
* Secure architecture design (no hardcoded secrets)

---

## DevSecOps Implementation

Security considerations were incorporated where applicable in the current stage, with further controls planned.

### Current

* ECR image scanning enabled (scan-on-push)
* IAM execution roles used for ECS tasks
* No hardcoded secrets in application code
* Centralized logging via CloudWatch

### Planned

* Secrets management with AWS Secrets Manager
* Static code analysis (e.g. Bandit)
* Dependency vulnerability scanning
* CI/CD security checks

---

## How It Works

### Current Flow

1. Build Docker image locally
2. Push image to Amazon ECR
3. ECS pulls image and runs container
4. Logs are sent to CloudWatch

### Future Flow

1. Developer pushes code to GitHub
2. CodePipeline triggers pipeline
3. CodeBuild builds Docker image
4. Image is pushed to ECR
5. ECS service updates automatically
6. Application served via ALB

---

## Project Structure

```
app/ → Flask application  
Dockerfile → Container build instructions  
pipeline/ → CI/CD configurations  
terraform/ → Infrastructure as Code  
docs/ → Architecture diagrams, screenshots and notes  
```

---

## Key Decisions

* ECS Fargate chosen over EC2-backed ECS to avoid infrastructure management
* AWS-native services used for tight integration and simplicity
* Minimal base Docker image used for security and efficiency
* CloudWatch used for centralized logging and observability

---

## Phase 1: Local Container Setup

* Built a Flask API with 3 endpoints
* Containerized the application using Docker
* Ran and tested locally using Postman
* Verified container logs and execution

---

## Phase 2: Image Pushed to ECR

* Created ECR repository
* Enabled image scanning (scan-on-push)
* Tagged and pushed Docker image
* Verified image in AWS

---

## Phase 3: Deployment on ECS Fargate

### Implementation

* Created CloudWatch log group
* Created ECS task execution role
* Created and registered task definition
* Created ECS cluster
* Configured networking (used default VPC, subnets, security group)
* Created ECS service with desired count of 1
* Enabled public IP for initial testing
* Verified application via public endpoint

### Deployment Result

* Service status: ACTIVE
* Launch type: FARGATE
* Desired tasks: 1
* Running tasks: 1
* Pending tasks: 0
* Deployment state: COMPLETED

### Key Concepts Learned

* Task Definition: blueprint for container execution
* Task: running instance of a task definition
* Service: maintains desired number of tasks
* Cluster: logical grouping of ECS resources
* Fargate: serverless compute for containers

---

## Lessons Learned

* Difference between Docker images and running containers
* How ECS uses task definitions as deployment blueprints
* Importance of IAM execution roles for ECR and logging
* How Fargate abstracts infrastructure management
* Basic networking considerations (subnets, security groups, public IP)

---

## Troubleshooting

* Container startup issues : checked CloudWatch logs
* Image pull errors : verified ECR URI and permissions
* Connectivity issues : verified port 5000 and security group rules

---
## Notes

For this initial deployment:

* Default VPC was used
* Public IP assigned for testing
* Direct access to container enabled

### Planned Improvements

* Introduce an Application Load Balancer (ALB)
* Restrict direct public access
* Improve network segmentation
* Implement Infrastructure as Code using Terraform
* Add CI/CD pipeline

---
## Evidence

* ECS service reached steady state
* Task successfully running (1/1)
* Application tested successfully
* Logs available in CloudWatch

## Phase 4: Application Load Balancer Integration

### Implementation
- Created an internet-facing Application Load Balancer (ALB)
- Created a target group with target type `ip` (required for ECS Fargate)
- Configured health checks on `/health`
- Added HTTP listener on port 80
- Updated ECS service to register tasks with the target group
- Restricted task access to only allow traffic from ALB security group

### Result
- Application successfully accessed via ALB DNS endpoint
- Verified endpoints using Postman
- Target group health checks passing

### Architectural Improvement
Previous:
Direct public access to ECS task via public IP

Current:
Internet to ALB to ECS Fargate to CloudWatch (Logs)

## What this does
- Removes direct public exposure to containers
- Enables scalability and load balancing
- Provides a foundation for HTTPS and domain routing
- Aligns with production-grade architecture patterns
---

## Author

Built as part of my transition into cloud-native DevSecOps engineering, focusing on real-world, production-like workflows.
