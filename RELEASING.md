# Releasing

## One-time setup: PyPI Trusted Publishing

`.github/workflows/publish-pypi.yml` publishes to PyPI on every GitHub
Release, using PyPI's [Trusted Publishing](https://docs.pypi.org/trusted-publishers/)
(OIDC) — no API token to create, store, or rotate. This needs a one-time
setup step on PyPI's side, by whoever owns the `sparkfly` PyPI project:

1. Go to https://pypi.org/manage/project/sparkfly/settings/publishing/
2. Add a new trusted publisher:
   - Owner: `growth-operations`
   - Repository name: `sparkfly-api-client`
   - Workflow filename: `publish-pypi.yml`
   - Environment name: `pypi`
3. Save. No further setup needed — the workflow already requests the
   matching `pypi` environment and OIDC token.

Until this is done, the publish job will fail with an authentication
error (the test job still runs and passes fine — only the publish step
needs this).

## Cutting a release

1. Edit `common_v1.yaml` for the spec change.
2. Bump `packageVersion` in `openapi-config.yaml` to the new version.
3. `make generate-client` to regenerate the client from the spec.
4. **Also bump `version` in `pyproject.toml` by hand** — the generator's
   own ignore file (`.openapi-generator-ignore`) excludes it, so it never
   gets updated by step 3. Forgetting this step means `python -m build`
   silently builds the *old* version number even though `setup.py` and
   everything else correctly shows the new one.
5. Run the test suite (`pytest test/ tests/`) and confirm everything
   passes.
6. Commit, push, tag (`git tag vX.Y.Z && git push origin vX.Y.Z`).
7. Create a GitHub Release from that tag — this triggers
   `publish-pypi.yml`, which runs the test suite again and publishes to
   PyPI if it passes.
