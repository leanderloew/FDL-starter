import os
env_path = "../{{cookiecutter.project_name}}/.envs/"
os.makedirs("../{{cookiecutter.project_name}}/data", exist_ok=True)
os.makedirs(env_path, exist_ok=True)

with open(env_path+"gen.env", "w") as file:
    file.write("PYTHONPATH = /app\n"
               "IS_LOCAL = True\n"
               "AWS_ACCESS_KEY_ID={{cookiecutter.aws_local_key_id}}\n"
               "AWS_SECRET_ACCESS_KEY={{cookiecutter.aws_local_secret_key}}")

with open(env_path+"dev.env", "w") as file:
    file.write("SENTRY_DNS = {{cookiecutter.sentry_dev}}\n"
               "POSTGRES_PASSWORD = {{cookiecutter.postgres_password_dev}}\n"
               "POSTGRES_HOST = {{cookiecutter.postgres_host_dev}}}\n")

with open(env_path+"prod.env", "w") as file:
    file.write("SENTRY_DNS = {{cookiecutter.sentry_prod}}\n"
               "POSTGRES_PASSWORD = {{cookiecutter.postgres_password_prod}}\n"
               "POSTGRES_HOST = {{cookiecutter.postgres_host_prod}}}\n")
