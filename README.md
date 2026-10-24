# CSC 325 — Module 8: First CI/CD Pipeline

A small Django REST Framework study-room booking API with a four-stage GitHub Actions pipeline.

## API
- `GET /api/rooms/` lists rooms.
- `GET /api/rooms/<id>/` returns a room's name, building, capacity, and availability.

## Local setup
Use Python 3.12:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py test --verbosity 2
python manage.py runserver
```

Open `http://127.0.0.1:8000/api/rooms/`. An empty list is expected before rooms are added.

## Continuous integration and simulated deployment
The workflow at `.github/workflows/csc325_ci_cd.yml` runs on pushes to `main` and pull requests targeting `main`.

The four separately named jobs are **Setup**, **Dependencies**, **Test**, and **Deploy**, linked with job dependencies. Deploy runs only after successful tests on a `main` push and prints the permitted simulated-deployment message. **The API is not publicly hosted**; actual deployment is optional extra credit for this assignment.

## Recording
Create a feature branch and make a small API change plus a test. Keep it unpushed until recording. Record the local tests, commit and push to the feature branch, open a pull request and merge into protected `main`, then show the resulting four green jobs on the push-to-main workflow run.

## Submission
Provide (1) your narrated video, (2) the public repository URL, (3) the link to the green workflow run triggered on camera, and (4) the link to that run's Deploy job as evidence of the assignment-approved `echo` simulation.
