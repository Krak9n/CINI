The key to the problem is to run recursive grep search on the repo. It will go over all of the commits and will find exact match.  
  
```bash
	git grep -r "flag{" $(git rev-list --all)
```