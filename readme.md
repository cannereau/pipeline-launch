# AWS Launch Pipeline with Lambda function

This project presents a complete way to build a Lambda function able to launch a CodePipeline

## Usage
You have to provide the *merged pipeline*'s name in the __User Parameters__ of the pipeline's **Action** in JSON form :
*{"PipelineName":"my.pipeline"}*