# OTC Engineers 
# Data Warehousing Project
Group members - Pujan Patel, Samantha Soto, and Sanjit Guliani
## Description
This project is a data warehousing solution designed to consolidate, transform, and store large volumes of data from various sources for analytical purposes. It aims to provide a centralized repository for business intelligence and reporting.

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Extract, Transform, Load (ETL) processes for data integration.
- Support for various data sources, including databases, APIs, and flat files.
- Data modeling and schema design for optimal query performance.
- Scheduled data refresh and automation.
- Integration with analytics and reporting tools.

## Architecture
The data warehousing project follows a star schema architecture with a central data warehouse and surrounding data marts. It leverages [ETL tool] for data integration and [Database System] for storage.

![Architecture Diagram](docs/architecture.png)

## Getting Started
### Prerequisites
- [Java](https://www.java.com/) installed
- [ETL Tool](link-to-etl-tool) installed
- [Database System](link-to-database) installed

### Installation
1. Clone the repository.
2. Configure the ETL tool with the provided configuration file (`etl-config.yaml`).
3. Create the necessary database tables using the provided SQL scripts (`scripts/create_tables.sql`).

## Usage
To run the ETL process and update the data warehouse:

```bash
./run_etl.sh
