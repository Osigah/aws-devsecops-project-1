 <h3> AWS DevSecOps Project 1 – Secure CI/CD Pipeline for Containerized Flask App </h3>

## Overview

This project demonstrates a complete DevSecOps workflow on AWS, where a containerized Python (Flask) application is built, stored, deployed, and monitored using AWS-native services.

The goal is to simulate a real-world cloud deployment pipeline with integrated security practices, rather than just deploying an application.

## Architecture

GitHub → CodePipeline → CodeBuild → ECR → ECS Fargate → ALB → CloudWatch

## Services Used

- Amazon ECS (Fargate)
- Amazon ECR
- AWS CodePipeline
- AWS CodeBuild
- Amazon CloudWatch
- AWS Secrets Manager
- Terraform (coming in later phase)

## Features

- Containerized Flask application using Docker
- Image storage in Amazon ECR with scan-on-push enabled
- Deployment on ECS Fargate (serverless containers)
- Centralized logging using CloudWatch
- Environment variables injected into containers
- Secure architecture design (no hardcoded secrets)

## DevSecOps Implementation

Security was integrated across multiple stages of the pipeline:

Code Stage:
- Basic security checks using Python tooling (planned extension)

Build Stage:
- ECR image scanning enabled to detect vulnerabilities

Deployment Stage:
- IAM roles configured with least privilege

Runtime Stage:
- Secrets stored securely (planned with AWS Secrets Manager)
- Logging and monitoring via CloudWatch

This approach ensures security is embedded throughout the delivery lifecycle rather than added at the end.

## How It Works

1. Developer pushes code to GitHub
2. CodePipeline triggers the pipeline
3. CodeBuild builds Docker image
4. Image is pushed to ECR
5. ECS service pulls new image and deploys
6. Application runs behind a load balancer
7. Logs and metrics are sent to CloudWatch

## Project Structure

- app/ --> Flask application
- Dockerfile --> Container build instructions
- pipeline/ --> CI/CD configurations
- terraform/ --> Infrastructure as Code (coming next)
- docs/ --> Architecture diagrams and notes

## Key Decisions

- ECS Fargate chosen over EC2-backed ECS to avoid infrastructure management
- AWS-native CI/CD tools used for tight integration and simplicity
- Minimal base Docker image used for security and efficiency
- Logs centralized in CloudWatch for observability

## Future Improvements

- Add Terraform for full infrastructure automation
- Integrate vulnerability scanning tools (e.g. Trivy)
- Implement Secrets Manager for runtime secrets
- Introduce automated testing stage in pipeline
- Add ALB with HTTPS

## Day 1: Local Container Setup

- Built a Flask API with 3 endpoints
- Containerized the application using Docker
- Ran and tested locally using Postman
- Verified container logs and execution

Screenshots available in docs/screenshots/

## Day 2: Image pushed to ECR
- Created ECR repository
- Enabled image scanning
- Tagged and pushed Docker image
- Verified image in AWS

Screenshots available in docs/screenshots/

🔹 Author

Built as part of my transition into cloud-native DevSecOps engineering.