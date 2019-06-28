from setuptools import setup

setup(
    name='hotcidr-dash',
    version='0.1.0',
    author='',
    author_email='stephan.kemper@viasat.com',
    packages=['hotcidrdash'],
    license='Apache License 2.0',
    description="Web Dashboard for HotCIDR",
    install_requires=[
        "Flask >= 0.10.1",
        "Flask-Assets >= 0.9",
        "Flask-SQLAlchemy >= 1.0",
        "Flask-WTF >= 0.9.5",
        "HotCIDR >= 0.1.0",
        "humanize >= 0.5",
        "redis >= 2.9.1",
        "requests >= 2.3.0",
        "python-crontab >= 1.8.1",
        "croniter >= 0.3.5",
        "python-ldap >= 2.4.16",
        "celery >= 3.1.18"
    ],
)
