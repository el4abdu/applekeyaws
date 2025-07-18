#!/bin/bash

# AWS Full Setup Script for Apple Music Key Generator

# Exit on any error
set -e

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo -e "${GREEN}[AWS SETUP]${NC} $1"
}

# Error handling function
error() {
    echo -e "${YELLOW}[ERROR]${NC} $1"
    exit 1
}

# Verify AWS CLI is installed
verify_aws_cli() {
    log "Checking AWS CLI..."
    if ! command -v aws &> /dev/null; then
        error "AWS CLI is not installed. Please install it first."
    fi
    aws --version
}

# Create IAM Role for Elastic Beanstalk
create_eb_role() {
    log "Creating Elastic Beanstalk Service Role..."
    aws iam create-role \
        --role-name apple-key-generator-eb-role \
        --assume-role-policy-document file://eb-role-trust-policy.json

    aws iam attach-role-policy \
        --role-name apple-key-generator-eb-role \
        --policy-arn arn:aws:iam::aws:policy/service-role/AWSElasticBeanstalkService
}

# Create IAM Role Trust Policy
create_role_trust_policy() {
    log "Creating Role Trust Policy..."
    cat > eb-role-trust-policy.json << EOL
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "elasticbeanstalk.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOL
}

# Create S3 Bucket for Application Deployment
create_s3_bucket() {
    log "Creating S3 Bucket for Application..."
    BUCKET_NAME="apple-key-generator-$(date +%s)"
    aws s3 mb s3://$BUCKET_NAME
    echo $BUCKET_NAME > s3_bucket_name.txt
}

# Prepare Elastic Beanstalk Application
prepare_eb_application() {
    log "Creating Elastic Beanstalk Application..."
    aws elasticbeanstalk create-application \
        --application-name apple-music-key-generator \
        --description "Apple Music Key Generator Web Application"
}

# Create Elastic Beanstalk Environment
create_eb_environment() {
    log "Creating Elastic Beanstalk Environment..."
    aws elasticbeanstalk create-environment \
        --application-name apple-music-key-generator \
        --environment-name apple-key-generator-env \
        --solution-stack-name "64bit Amazon Linux 2 v3.3.13 running Python 3.8" \
        --option-settings file://eb-environment-settings.json
}

# Create EB Environment Settings
create_eb_environment_settings() {
    log "Creating Elastic Beanstalk Environment Settings..."
    cat > eb-environment-settings.json << EOL
[
    {
        "Namespace": "aws:autoscaling:launchconfiguration",
        "OptionName": "InstanceType",
        "Value": "t2.micro"
    },
    {
        "Namespace": "aws:elasticbeanstalk:environment",
        "OptionName": "EnvironmentType",
        "Value": "SingleInstance"
    }
]
EOL
}

# Main Deployment Function
main() {
    verify_aws_cli
    create_role_trust_policy
    create_eb_role
    create_s3_bucket
    prepare_eb_application
    create_eb_environment_settings
    create_eb_environment

    log "🎉 AWS Deployment Setup Complete! 🎉"
}

# Run the main function
main 