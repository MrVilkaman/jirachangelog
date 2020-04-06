import json
import os
from dataclasses import dataclass
from getpass import getpass


@dataclass
class Credentials:
    login: str
    password: str
    jira_url: str


class CredentialsLoader:

    def load(self, creds_file_path: str = None) -> Credentials:
        if creds_file_path is not None:
            return self._load_credentials_from_file(creds_file_path)

        creds: Credentials
        try:
            creds = self._load_from_os()
        except ValueError as e:
            creds = self._load_from_manual_enter()

        return creds

    @staticmethod
    def _load_credentials_from_file(file_name: str) -> Credentials:
        def extract_field(raw, field_name: str) -> str:
            field = raw[field_name]
            if field is None:
                raise ValueError("Cannot found {} field in credentials file {}".format(field_name, file_name))
            return field

        with open(file_name, "r") as creds_file:
            raw_creds = json.loads(creds_file.read())
            return Credentials(
                extract_field(raw_creds, "login"),
                extract_field(raw_creds, "password"),
                extract_field(raw_creds, "jiraUrl")
            )

    @staticmethod
    def _load_from_os() -> Credentials:
        def get_env(name: str) -> str:
            env = os.getenv('_JIRA_LOGIN')
            if env is None:
                raise ValueError("Cannot found {} environment variable".format(name))
            return env
        return Credentials(
            get_env("JIRA_LOGIN_KEY"),
            get_env("JIRA_PASSWORD_KEY"),
            get_env("JIRA_BASE_URL_KEY")
        )

    @staticmethod
    def _load_from_manual_enter() -> Credentials:
        url = input("Enter jira url:")
        login = input("Enter jira login:")
        password = getpass("Enter jira password:")
        return Credentials(login, password, url)
