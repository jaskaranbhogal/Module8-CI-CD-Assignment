# CSC 325 — Module 8: First CI/CD Pipeline

A small Django REST Framework study-room booking API with a four-stage GitHub Actions pipeline.

## API
- `GET /api/rooms/` lists rooms.
- `GET /api/rooms/<id>/` returns room name, building, capacity, and availability.
- The recording's planned feature patch adds `GET /api/status/` with its own automated test.

## Local setup
Use Python 3.12:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py test --verbosity 2
python manage.py runserver
```

Open `http://127.0.0.1:8000/api/rooms/`. An empty list is expected until rooms are created.

## GitHub Actions — Setup, Dependencies, Test, Deploy
The single workflow at `.github/workflows/csc325_ci_cd.yml` runs on pushes to `main` and `feature/**` and on pull requests targeting `main`.

It has four separate sequential jobs: **Setup**, **Dependencies**, **Test**, and **Deploy**. Failed tests fail the pipeline; Deploy executes only after a successful Test job **on a push to main**.

### GitHub Pages deployment
The Deploy job now publishes a **static API demonstration** to GitHub Pages. The build script (`scripts/build_pages.py`) starts Django locally inside the Actions runner, seeds one example room, requests the API, and creates HTML showing the resulting JSON responses. The generated site is published as a Pages artifact. The planned `/api/status/` endpoint will automatically appear when that feature gets merged, so the deployed page visibly reflects the code change.

**GitHub Pages cannot run the Django backend.** The website contains **build-time snapshots** and clearly says it is not a live API server. For actual hosted Python API execution, use a Python-capable hosting provider instead.

To activate the site, open **Settings → Pages → Build and deployment → Source → GitHub Actions**. GitHub Pages hosting must be enabled for the deploy action to succeed. The site address, once live, will appear as the environment URL in the Deploy job.

You can preview the generated site locally after installing dependencies and running `python manage.py migrate`:

```bash
python scripts/build_pages.py
python -m http.server 8080 --directory _site
```

## Recording
Use the existing `feature/api-status-demo` branch. Apply the prepared code-and-test patch without pushing it yet. During your screen recording: explain the workflow, show and run the tests, commit and push the feature branch, open and merge a PR to the protected `main` branch, show the new green four-stage pipeline, then open the Pages URL to show `GET /api/status/` in the generated snapshot.

## Submission
Provide (1) your narrated video, (2) the public repository URL, (3) the specific green `main` workflow run initiated by the on-camera merge, and (4) the Pages URL. Clearly label the Pages site a static demonstration, not an operational Django API.
