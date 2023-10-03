# Import the required module for setup
import setuptools

# Read the content of the README file to use it as a long description for the package
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Specify the version of the package
__version__ = "0.0.0"

# Constant specifying the metadatas of the package
REPO_NAME = "Text-Summarization"
AUTHOR_USER_NAME = "vbabua"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "babuvadakemu@gmail.com"

# Call the setup function to specify the properties of the package
setuptools.setup(
    # Name of the package
    name=SRC_REPO,

    # Version of the package
    version=__version__,

    # Name of the package author
    author=AUTHOR_USER_NAME,

    # Email of the package author
    author_email=AUTHOR_EMAIL,

    # Short description of the package
    description="A small python package for NLP app",

    # Detailed description of the package (typically the content of README.md)
    long_description=long_description,

    # Specify the type of the long description
    long_description_content_type="text/markdown",

    # URL to the source code of the package
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",

    # Additional URLs related to the project, like bug tracker
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },

    # Specify the directory where the package source code is located
    package_dir={"": "src"},

    # Automatically discover and include all packages in the specified directory
    packages=setuptools.find_packages(where="src"),

    # Classifiers help users find your project by categorizing it.
    classifiers=[
        "Programming Language :: Python :: 3",  # Indicate that the package is written in Python 3
        "License :: OSI Approved :: MIT License",  # Indicate the type of license used
        "Operating System :: OS Independent",  # Indicate that the package is OS independent
        # You can add more classifiers as needed
    ],

    # Specify the minimum python version required to run this package
    python_requires='>=3.6',

    # List dependencies that will be installed along with this package
    install_requires=[
        # e.g., 'requests>=2.0.0', 'numpy>=1.18.0'
    ],

    # Specify the license type for the package
    license="MIT",

    # Specify the location of the license file in the package
    license_file="LICENSE",

    # If the package provides any console commands, specify them here
    entry_points={
        'console_scripts': [
            # Example: 'your_script_name=your_package.module:function'
        ],
    }
)