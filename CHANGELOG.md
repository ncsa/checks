# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## 1.0.1 - 2022-07-25

### Added
- add support for standard postgresql environment variables [#2](https://github.com/ncsa/checks/issues/2)
- GitHub action to create docker file [#3](https://github.com/ncsa/checks/issues/3)

### Changed
- more verbose logging in case of check_url, thanks @khk-globus
- changed master branch to main branch.
- changed PG_URI and PG_TABLE to be PGURI and PGTABLE to be consistent with other PG variables.
- environment variable and argument in checks.json are flipped around to allow for deprecated environment variables.

## 1.0.0 - 2020-08-07

### Added
- support for RabbitMQ
- support for MongoDB
- support for URL
- support for PostgreSQL
