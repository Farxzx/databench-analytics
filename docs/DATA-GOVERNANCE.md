\# Data Governance Policy



\## Purpose



This document defines data governance controls for employee and sales datasets.



\## Data Classification



\* Employee Names: Internal

\* Employee Emails: Sensitive

\* Salary Information: Confidential

\* Sales Data: Internal



\## Access Control



\* HR Analyst: Access to employee records

\* Sales Analyst: Access to sales records and masked employee data

\* Executive: Read-only access to summarized information



\## Data Masking



\* Employee emails are masked before being exposed to non-HR users.

\* Salary values are converted into salary bands.



\## Audit Logging



All critical actions are recorded in audit logs including:



\* SELECT

\* INSERT

\* UPDATE

\* DELETE



\## Data Retention



Data should be retained according to organizational policy and reviewed periodically.



