# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## 1.1.1 - 2025-08-18

### Changed
- Update psycopg2-binary to 2.9.10

## 1.1.0 - 2024-11-11

### Added
- building arm image

### Changed
- using python 3.11
- updated docker github action

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
