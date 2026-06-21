\# Supabase RLS Policies



\## HR Analyst Policy



Purpose:

Allow HR analysts to view employee information including salaries and performance data.



Permissions:



\* SELECT on employees table

\* No DELETE permission

\* No DROP permission



\## Sales Analyst Policy



Purpose:

Allow sales analysts to access sales data but restrict access to raw salary information.



Permissions:



\* SELECT on sales table

\* View masked employee information only

\* Salary values exposed as salary bands



\## Executive Policy



Purpose:

Provide read-only access to aggregated business reports.



Permissions:



\* Read aggregated views only

\* No direct access to employee table

\* No update, insert, or delete permissions



\## Security Notes



\* Sensitive employee emails are masked.

\* Salary values are categorized into bands.

\* Access activities are recorded in audit logs.

\* Least-privilege access principle is applied.



