#!/bin/bash
# The first stage submits the main branch first
git clone https://kernel.googlesource.com/pub/scm/linux/kernel/git/torvalds/linux
cd linux

git remote add google ssh://xxx@source.developers.google.com:2022/p/xxx/r/linux

REMOTE=google
BRANCH=$(git rev-parse --abbrev-ref HEAD)
BATCH_SIZE=100

# check if the branch exists on the remote
if git show-ref --quiet --verify refs/remotes/$REMOTE/$BRANCH; then
    # if so, only push the commits that are not on the remote already
    range=$REMOTE/$BRANCH..HEAD
else
    # else push all the commits
    range=HEAD
fi

# count the number of commits to push
n=$(git log --first-parent --format=format:x $range | wc -l)
echo $BRANCH has $n commits
# push each batch
for i in $(seq $n -$BATCH_SIZE 1); do
    # get the hash of the commit to push
    h=$(git log --first-parent --reverse --format=format:%H --skip $i -n1)
    echo "Pushing $h..."
    git push $REMOTE ${h}:refs/heads/$BRANCH
done
# push the final partial batch
git push $REMOTE HEAD:refs/heads/$BRANCH

# The second stage processes tag information
git push -u google --all
git push -u google --tags

# git push --mirror google
cd ..
git clone --bare https://kernel.googlesource.com/pub/scm/linux/kernel/git/torvalds/linux
cd linux.git
git remote add google ssh://xxx@source.developers.google.com:2022/p/xxx/r/linux
git push --mirror google
