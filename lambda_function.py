import boto3

build = boto3.client('codebuild')
commit = boto3.client('codecommit')

def lambda_handler(event, context):
    
    #get details of code build result
    if event["detail"]["event"] == "pullRequestCreated" or event["detail"]["event"] == "pullRequestSourceBranchUpdated":
        event["detail"]["pullRequestId"]
        event["detail"]["destinationReference"]
        event["detail"]["sourceReference"]
        event["detail"]["destinationCommit"]
        event["detail"]["sourceCommit"]
        event["detail"]["repositoryNames"][0]
        
        targetBranch = event["detail"]["destinationReference"].split('/')[2]
        sourceBranch = event["detail"]["sourceReference"].split('/')[2]

    #start code build with updated parameters from the pull request event
        startBuild = build.start_build(
                    projectName=event["detail"]["repositoryNames"][0],
                    sourceVersion=sourceBranch,
                    environmentVariablesOverride=[
                            {
                                  'name': 'pullRequestId',
                                  'value': event["detail"]["pullRequestId"],
                                  'type': 'PLAINTEXT'
                            },
                            {
                                  'name': 'targetBranch',
                                  'value': targetBranch,
                                  'type': 'PLAINTEXT'
                            },
                            {
                                  'name': 'sourceBranch',
                                  'value': sourceBranch,
                                  'type': 'PLAINTEXT'
                            },
                            {
                                  'name': 'destinationCommit',
                                  'value': event["detail"]["destinationCommit"],
                                  'type': 'PLAINTEXT'
                            },
                            {
                                  'name': 'sourceCommit',
                                  'value': event["detail"]["sourceCommit"],
                                  'type': 'PLAINTEXT'
                            },
                            {
                                  'name': 'repositoryName',
                                  'value': event["detail"]["repositoryNames"][0],
                                  'type': 'PLAINTEXT'
                            }]
                    )
                    
        
        print(startBuild)
