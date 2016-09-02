# mother-of-issues

A Python command line tool that creates GitHub issues with the same title & body in multiple repositories. 

_Handy if you manage multiple repositories that require the same update on occasion._

#### Additional Features

* **Filter by category:** assign categories to repositories in the [repository data](#repository-data) file, when you run the script you can provide a category to specify a subset of repositories to update

## Prerequisites

A GitHub [access token](https://help.github.com/articles/creating-an-access-token-for-command-line-use/) from an account that has `PULL` access to the target repositories must be created.

1. Go to: https://github.com/settings/tokens
2. Generate a token with access to the following scopes according to your needs: `repo` and `public_repo`
3. Make a copy of [`settings.sample`](settings.sample) and rename to `settings.txt`
4. Assign the access token created in step 2 to `github_access_token` in `settings.txt`, Example:

```
github_access_token=[GITHUB_ACCESS_TOKEN_HERE]
```

## Usage

1. Confirm that the repos listed in [`repos.json`](repos.json) are accurate
2. Add the issue title to line 1 of [`issue.txt`](issue.txt)
3. Add the issue body to lines 2..n of [`issue.txt`](issue.txt) (ie. the title and body are separated by a newline)
4. Run the script from the root directory of the project...**there is no UNDO, proceed with caution**: 

```bash
python main.py [category]
```

**[category]** _case-sensitive_ should be replaced with either `all` to update all repositories or chose from your own categories that you have defined and any repository in [`repos.json`](repos.json) that match the given category will be updated.

## Repository Data

Repositories are listed in [`repos.json`](repos.json), each library is represented as a JSON object with the following structure:

```
{ 
  "name": "github-repo-name",
  "owner": "github-repo-owner",
  "category": "category-name"
}
```

## Dependencies

* Python Version: see [`runtime.txt`](runtime.txt)
* Requirements: see [`requirements.txt`](requirements.txt)
