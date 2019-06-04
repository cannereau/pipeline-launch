# AWS Launch Pipeline with Lambda function

This project presents a complete way to build a Lambda function able to launch a CodePipeline.

Sometimes, it can be useful to launch a pipeline from another one.

It can be done easily with a Lambda function.

## Usage

* In your *main pipeline* create a new **Action** using **AWS Lambda** provider.
* Choose the Lambda function named *pipeline-launch* built by the **pipeline.yml** and the **pipeline.bat** provided by this project
* Then, write down the *target pipeline*'s name in the **User Parameters** of the pipeline's **Action** in JSON form :

        {"PipelineName":"my.pipeline"}
