
# devops-nauka

A small project I'm using to learn Docker and CI/CD. It's a simple Flask app with a few endpoints, packaged into a Docker container.

## Run locally

```bash
docker compose up -d --build
```

The app runs at http://localhost:5000. You can check `/health` and `/version` to see if it's working.

To stop it:

```bash
docker compose down
```

## Tests

```bash
pip install -r requirements.txt
python -m unittest discover -s tests -v
```

## CI/CD

I set up GitHub Actions to run the tests and build a Docker image. On pushes to `main`, the workflow also publishes the image to GitHub Container Registry (GHCR).

I'm using this repo to practice working with Docker, Docker Compose, GitHub Actions and debugging failed builds.
