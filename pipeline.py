import json
import logging
import boto3

# cold start
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info('INFO #000 : loading function...')
code_pipeline = boto3.client('codepipeline')

def launch(event, context):

    # starting handler
    logger.info('INFO #001 : received event : {}'.format(event))

    # get the current pipeline job
    try:
        job = event['CodePipeline.job']
        logger.info('INFO #002 : current pipeline job id : {}'.format(job['id']))
    except Exception as e:
        logger.error('ERROR #101 : lambda is missing event[CodePipeline.job]')
        raise e

    # retrieve pipeline name to launch
    try:
        userparam = job['data']['actionConfiguration']['configuration']['UserParameters']
        logger.info('INFO #003 : UserParameters : {}'.format(userparam))
    except:
        return notify_failure(job['id'], 'ERROR #102 : lambda is missing job.action[UserParameters]')
    try:
        jsonparam = json.loads(userparam)
    except:
        return notify_failure(job['id'], 'ERROR #103 : invalid JSON in UserParameters')
    try:
        if jsonparam['PipelineName'].strip() == '':
            return notify_failure(job['id'], 'ERROR #104 : target PipelineName is empty')
        else:
            pipelinename = jsonparam['PipelineName']
            logger.info('INFO #004 : target PipelineName : {}'.format(pipelinename))
    except:
        return notify_failure(job['id'], 'ERROR #105 : target PipelineName is missing in UserParameters')

    # launch pipeline
    try:
        code_pipeline.start_pipeline_execution(name=pipelinename)
        return notify_success(job['id'], 'INFO #005 : pipeline started successfully')
    except:
        return notify_failure(job['id'], "ERROR #106 : starting pipeline failed : you should check PipelineName in UserParemeters")

def notify_success(id, message):
    logger.info(message)
    return code_pipeline.put_job_success_result(jobId=id)

def notify_failure(id, message):
    logger.error(message)
    return code_pipeline.put_job_failure_result(jobId=id, failureDetails={'message': message, 'type': 'JobFailed'})
