# Lesson 8: YouGile API projects

Six pytest checks for `POST /projects`, `PUT /projects/{id}` and
`GET /projects/{id}` (positive and negative for each method).

## Setup (Windows PowerShell)

Install: `python -m pip install pytest requests`

Create a YouGile account/company, then obtain an API key using the
[official API documentation](https://ru.yougile.com/api-v2#/).

Set environment variables **only in your local terminal**:

```powershell
$env:YOUGILE_API_TOKEN = "YOUR_PRIVATE_API_KEY"
# Optional if the account requires project users on creation:
$env:YOUGILE_USER_ID = "YOUR_YOUGILE_USER_UUID"
# Optional if you use a custom YouGile host:
$env:YOUGILE_API_URL = "https://yougile.com/api-v2"
python -m pytest lesson_08 -v
python -m flake8 lesson_08
```

Do not commit or send real keys, passwords or local configuration files.
The reviewer needs their own **API key** for a company in which they can
create and edit projects. If required, set the **user UUID** from that
company in `YOUGILE_USER_ID`.

## Test isolation and cleanup

Each positive test creates its own project with a unique title. The
fixture soft-deletes it via `PUT {"deleted": true}` after the test,
even on test failure. Negative tests use missing required data or
random unknown UUIDs, so they do not modify existing projects.

**Note:** This API documents no `DELETE /projects/{id}` endpoint, only
soft-deletion via PUT. Response status codes and error shapes must be
verified on a real YouGile account before handing in the homework.
Without `YOUGILE_API_TOKEN`, pytest skips the suite instead of reporting
false success.
