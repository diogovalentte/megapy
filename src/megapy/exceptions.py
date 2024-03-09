class CLIException(Exception):
    def __init__(
        self,
        msg=None,
        cli=None,
        cli_args=None,
        options=None,
        stdout=None,
        stderr=None,
    ):
        self.msg = msg
        self.cli = cli
        self.cli_args = cli_args
        self.options = options
        self.stdout = stdout
        self.stderr = stderr

        super().__init__(msg)

    def __str__(self):
        return f"""{self.msg}, on:
cli: '{self.cli}'
options: {self.options}
args: {self.cli_args}
stdout: '''
    {self.stdout}
'''
stderr: '''
    {self.stderr}
'''
"""