import boto3


class Client:
    """ Class for creating a boto3 client """

    def __init__(self, service, account, role, region):
        self.service = service
        self.account = account
        self.role = role
        self.region = region

    def get_assume_role_session(self, **args):
        """
        Use sts to assume into an iam role, and return
        a boto3 session

        Args:
            (list)**args: role name and session name
        Return:
            (boto3.Session): session details
        """
        client = boto3.client('sts')
        try:
            response = client.assume_role(**args)
            credentials = response['Credentials']
        except Exception as e:
            print(e)

        return boto3.Session(
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken']
        )

    def get_client(self):
        """
        Assume into an iam role, and return a boto client

        Returns:
            (boto3.Client)client: aws client
        """
        assume_role_arn = \
            'arn:aws:iam::{}:role/{}'.format(
                self.account,
                self.role
            )
        session = self.get_assume_role_session(
            RoleArn=assume_role_arn,
            RoleSessionName='session-name-here'
        )

        client = session.client(
            self.service,
            region_name=self.region
        )

        return client

