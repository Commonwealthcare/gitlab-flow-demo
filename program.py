# This script is only simulating a deployment script running in automated deployments.

import os

print("This is a simulation of deployment script written by Harivardhan.")
print("It accesses secrets and variables defined for the environment in Repo Settings as follows:\n")

DB_URL = os.getenv('DB_URL')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')

print("DB_URL: " + DB_URL)
print("DB_USERNAME: " + DB_USERNAME)
print("DB_PASSWORD: " + DB_PASSWORD)

print("Deployment completed.")

print("------------------------------------------------------------------------------------------------------------------")
print("Initial Commit - 10/30")

print("Fixing variables and adding parenthesis - 10/31")
print("Fixing variables part two - 10/31")
print("Accessing env variables - 10/31")
print("Added more env, checking approval - 10/31")
print("Testing personal branches - part two - 10/31")