## Amazon Api Gateway Custom Request Response

Handle arbitrary HTTP requests and send custom HTTP responses with API Gateway.

This repository accompanies a forthcoming blog post.

## License Summary

This sample code is made available under the MIT-0 license. See the LICENSE file.

## Usage

To deploy this example into your AWS account, either use the AWS CloudFormation console or the following AWS CLI commands:

```shell
aws cloudformation package --template-file echo.template --output-template-file packaged.template --s3-bucket <YOUR S3 BUCKET>

aws cloudformation deploy --template-file packaged.template --stack-name <YOUR STACK NAME> --capabilities CAPABILITY_IAM
```

Replacing `<YOUR S3 BUCKET>` with the name of an S3 bucket that should hold the deployment artefacts and `<YOUR STACK NAME>` with a name of your choice for the resulting CloudFormation stack.
