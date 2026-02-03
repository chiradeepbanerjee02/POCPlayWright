# Self-Hosted Runner Setup Guide

This guide will help you set up a self-hosted GitHub Actions runner for the POCPlayWright repository.

## Prerequisites

- A Linux/Windows/macOS machine with internet connectivity
- Administrator/root access to the machine
- GitHub account with appropriate repository permissions (admin or write access)

## Common Error: "Http response code: NotFound from POST https://api.github.com/actions/runner-registration"

This error typically occurs due to one of the following reasons:

1. **Incorrect Repository URL**: The repository URL format is wrong
2. **Repository Access**: You don't have permission to register runners for the repository
3. **Token Expiration**: The registration token has expired (tokens are valid for 1 hour)
4. **Repository Path**: Using organization URL instead of repository URL

## Correct Setup Steps

### Step 1: Navigate to Repository Settings

1. Go to your repository: `https://github.com/chiradeepbanerjee02/POCPlayWright`
2. Click on **Settings** (you need admin access)
3. In the left sidebar, click **Actions** → **Runners**
4. Click **New self-hosted runner**

### Step 2: Choose Your Operating System

Select the appropriate operating system for your runner machine.

### Step 3: Download and Configure Runner

**Important**: Use the EXACT repository-specific commands provided by GitHub, which will look like:

#### For Linux/macOS:

```bash
# Create a folder
mkdir actions-runner && cd actions-runner

# Download the latest runner package
curl -o actions-runner-linux-x64-2.311.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz

# Extract the installer
tar xzf ./actions-runner-linux-x64-2.311.0.tar.gz

# Create the runner and start the configuration experience
# CRITICAL: Use the exact URL shown in your GitHub repository settings
./config.sh --url https://github.com/chiradeepbanerjee02/POCPlayWright --token YOUR_TOKEN_HERE

# Last step, run it!
./run.sh
```

#### For Windows (PowerShell):

```powershell
# Create a folder under the drive root
mkdir actions-runner; cd actions-runner

# Download the latest runner package
Invoke-WebRequest -Uri https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-win-x64-2.311.0.zip -OutFile actions-runner-win-x64-2.311.0.zip

# Extract the installer
Add-Type -AssemblyName System.IO.Compression.FileSystem ; [System.IO.Compression.ZipFile]::ExtractToDirectory("$PWD/actions-runner-win-x64-2.311.0.zip", "$PWD")

# Create the runner and start the configuration experience
# CRITICAL: Use the exact URL shown in your GitHub repository settings
./config.cmd --url https://github.com/chiradeepbanerjee02/POCPlayWright --token YOUR_TOKEN_HERE

# Last step, run it!
./run.cmd
```

### Step 4: Configure Runner Labels

During configuration, you will be asked to enter labels. For this repository, the workflow expects:

- Label 1: `self-hosted` (automatically added)
- Label 2: `us14-acuo125` (as specified in the workflow)

Or you can press Enter to use default labels and update the workflow file to match.

### Step 5: Verify Configuration

After running the configuration:

1. The runner should appear in your repository's Settings → Actions → Runners page
2. Its status should show as "Idle" (green) when active
3. The runner should display the labels you configured

## Troubleshooting

### Error: "Http response code: NotFound"

**Solution 1: Verify Repository URL**
- Ensure you're using the FULL repository URL: `https://github.com/chiradeepbanerjee02/POCPlayWright`
- Do NOT use: organization URL, shortened URL, or incorrect repository name

**Solution 2: Check Permissions**
- Verify you have admin or write access to the repository
- Check repository settings allow self-hosted runners
- For organization repositories, check organization settings

**Solution 3: Generate Fresh Token**
- Registration tokens expire after 1 hour
- Always generate a new token from: Repository Settings → Actions → Runners → New self-hosted runner
- Copy and use the token immediately

**Solution 4: Repository Path Issues**
```bash
# CORRECT - Repository specific
./config.sh --url https://github.com/chiradeepbanerjee02/POCPlayWright --token TOKEN

# WRONG - Organization level (requires different permissions)
./config.sh --url https://github.com/chiradeepbanerjee02 --token TOKEN

# WRONG - Missing repository name
./config.sh --url https://github.com/chiradeepbanerjee02/ --token TOKEN
```

### Runner Not Showing in GitHub

1. Check if `run.sh` or `run.cmd` is still running
2. Verify network connectivity to github.com
3. Check firewall settings allow outbound HTTPS (port 443)
4. Review runner logs in the `_diag` folder

### Runner Offline After Setup

1. Restart the runner service:
   - Linux/Mac: `./run.sh`
   - Windows: `./run.cmd`
2. Or install as a service (see GitHub documentation)

## Running as a Service

### Linux (systemd):

```bash
# Install service
sudo ./svc.sh install

# Start service
sudo ./svc.sh start

# Check status
sudo ./svc.sh status
```

### Windows:

```powershell
# Install service (run as Administrator)
./svc.cmd install

# Start service
./svc.cmd start

# Check status
./svc.cmd status
```

## Updating Workflow Configuration

If you want to use different runner labels, update `.github/workflows/playwright-tests.yml`:

```yaml
jobs:
  test:
    runs-on: [self-hosted, your-custom-label]  # Update labels here
```

## Alternative: Use GitHub-Hosted Runners

If self-hosted runners are not required, you can modify the workflow to use GitHub-hosted runners:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest  # Use GitHub's hosted runner
```

## Security Considerations

1. **Never share runner tokens** - they provide access to your repository
2. **Secure your runner machine** - it will execute code from your repository
3. **Use dedicated machines** - don't use personal/production machines
4. **Keep software updated** - regularly update the runner application
5. **Monitor runner activity** - check logs and GitHub Actions usage

## Additional Resources

- [GitHub Actions Self-Hosted Runners Documentation](https://docs.github.com/en/actions/hosting-your-own-runners)
- [Adding Self-Hosted Runners](https://docs.github.com/en/actions/hosting-your-own-runners/adding-self-hosted-runners)
- [Using Self-Hosted Runners in a Workflow](https://docs.github.com/en/actions/hosting-your-own-runners/using-self-hosted-runners-in-a-workflow)

## Support

If you continue to experience issues:

1. Check the runner logs in the `_diag` folder
2. Verify GitHub Actions are enabled for the repository
3. Ensure your GitHub account has the necessary permissions
4. Contact repository administrators for access issues
