# Quick Reference: Setting Up Self-Hosted Runner

## TL;DR - Quick Fix for "NotFound" Error

The error `Http response code: NotFound from 'POST https://api.github.com/actions/runner-registration'` means you're using the wrong URL or token.

### Quick Fix Steps:

1. **Go to GitHub**:
   - Navigate to: https://github.com/chiradeepbanerjee02/POCPlayWright
   - Click: Settings → Actions → Runners → New self-hosted runner

2. **Get Fresh Token**:
   - GitHub will show you commands with a fresh token
   - **Token expires in 1 hour** - use it immediately!

3. **Use EXACT Repository URL**:
   ```bash
   # ✅ CORRECT
   ./config.sh --url https://github.com/chiradeepbanerjee02/POCPlayWright --token YOUR_TOKEN
   
   # ❌ WRONG - Missing repository name
   ./config.sh --url https://github.com/chiradeepbanerjee02 --token YOUR_TOKEN
   ```

4. **Set Runner Labels**:
   - When prompted, add label: `us14-acuo125`
   - Or update `.github/workflows/playwright-tests.yml` to match your labels

5. **Start Runner**:
   ```bash
   ./run.sh          # Linux/Mac
   ./run.cmd         # Windows
   ```

## Verification Checklist

- [ ] Used exact repository URL: `https://github.com/chiradeepbanerjee02/POCPlayWright`
- [ ] Token is fresh (generated within last hour)
- [ ] Have admin or write access to repository
- [ ] Runner appears in GitHub Settings → Actions → Runners
- [ ] Runner status shows as "Idle" (green)
- [ ] Labels match workflow requirements: `self-hosted, us14-acuo125`

## Still Having Issues?

See full documentation: [RUNNER_SETUP.md](RUNNER_SETUP.md)

## Alternative: Use GitHub-Hosted Runner

Don't want self-hosted? Edit `.github/workflows/playwright-tests.yml`:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest  # Replace line 12
```

Then remove the self-hosted runner requirement entirely.
