from setuptools import setup, find_packages

setup(
    name='streamlit-gemini-chatbot',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'os',
        'streamlit',
        'google-generativeai',
    ],
    author='Sambonic',
    description='A simple chatbot using Streamlit and Gemini API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Sambonic/streamlit-gemini-chatbot',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
