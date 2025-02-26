from setuptools import setup, find_packages

# Read dependencies from requirements.txt
with open('requirements.txt') as f:
    requirements = f.readlines()

# Strip any extra whitespace or newlines
requirements = [r.strip() for r in requirements]

setup(
    name='Jarvis',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,  
    author="Priyanshu Ranjan",
    author_email="priyanshuranjan13032003@gmail.com",
    description="A brief description of your project",
    url="https://github.com/yourusername/yourproject",
)
