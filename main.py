from dotenv import load_dotenv
from cli.root_cli import run_cli

load_dotenv(dotenv_path=".env")

if __name__ == "__main__":
    run_cli()
