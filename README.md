# Job Trend Visualizer
## Introduction
Implement a distributed web crawler via Scrapy, Redis, Graphite, MongoDB and D3.js - Mongo cluster is for low level data storage, Redis is for distribution, Graphite is for monitoring crawler status, and D3 is for job information visualization and job moving trend prediction.
## Background Information and Motivation
The number of jobs indicates the development of one industry. Showing how job number increase/decrease and how job move to demonstrate an industry or a city's economical status and potential to a certain industry. I hope is tool will be helpful to people who want to find maybe next silicon valley.
## Technique details
### low-level storage
Initially, MySql is the first option. However, D3.js library only supports Json or csv format and MySql is hard to export json (as far as I know). So MongoDB has been used.
### strategies to prevent crawler from banning
### scheduler optimization
