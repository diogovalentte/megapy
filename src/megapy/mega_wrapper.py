import subprocess
from time import sleep

from megapy.exceptions import BandwithLimitException, CLIException


class Mega:
    def _get_options_list(self, options: dict | None):
        options_list = list()
        if not options:
            return options_list
        for option, value in options.items():
            if not option.startswith("-"):
                raise ValueError(f"Option {option} should start with '-' or '--'")
            if value is not None:
                option = f"{option}={value}"
            options_list.append(option)

        return options_list

    def _get_args_list(self, args: list | None):
        if not args:
            return list()
        return args

    def execute(
        self,
        cli: str,
        args: list | None = None,
        options: dict | None = None,
    ):
        """Execute a command in the shell.

        Args:
            cli (str): The CLI to be executed.
            args (list | None, optional): The command/subcommand arguments. Defaults to None.
            options (dict | None, optional): The command/subcommand options, like '--project', '--organization'. Defaults to None.
                - The options in this argument will be used instead of the class init arguments.

        Returns:
            (str): The command output.
        """
        commands_list = [
            cli,
        ]

        options_list = self._get_options_list(options)
        commands_list.extend(options_list)

        args_list = self._get_args_list(args)
        commands_list.extend(args_list)

        result = subprocess.run(args=commands_list, stdout=subprocess.PIPE, text=True)

        try:
            result.check_returncode()
        except subprocess.CalledProcessError:
            raise CLIException(
                "Failed to execute CLI",
                cli,
                args,
                options,
                result.stdout,
                result.stderr,
            )

        output = result.stdout

        return output

    def download_url(self, url: str, dest_folder: str, retries: int = 0):
        """Download a file from a URL.
        If the bandwith limit is reached, it'll try again `retry` times, with a space of 1 hour between the retries.

        Args:
            url (str): The URL to download the file from.
            dest_folder (str): The destination folder to save the file.
            retries (int, optional): The number of retries if the download fails. Defaults to 0.

        Raises:
            BandwithLimitException: If the bandwith limit is reached.
        """
        cli = "mega-get"
        args = [url, dest_folder]

        retries += 1
        while True:
            try:
                self.execute(cli, args)
                break
            except CLIException as e:
                if retries > 0:
                    retries -= 1
                    sleep(3600)
                    continue
                if (
                    "You have reached your bandwith quota. To circumvent this limit, you can upgrade to Pro, which will give you your own bandwidth package and also ample extra storage space."
                    in str(e.stdout)
                ):
                    raise BandwithLimitException()
                raise e
