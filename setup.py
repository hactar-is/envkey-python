from setuptools import setup

setup(
    name="envkey",
    version="2.4.2",
    description="Transitional version of EnvKey 2.4.2 with support for loading from phase.dev",
    url="https://github.com/envkey/envkey-python",
    keywords=[
        "security",
        "secrets management",
        "configuration management",
        "environment variables",
        "configuration",
        "python",
    ],
    author="Hactar",
    author_email="systems@hactar.is",
    license="MIT",
    packages=["envkey"],
    package_data={"envkey": ["ext/?/*"]},
    include_package_data=True,
    install_requires=[
        "phase-dev>=2.1.0",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
    ],
    zip_safe=False,
)
