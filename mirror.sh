#!/bin/bash
# The first stage submits the main branch first
git clone git://gcc.gnu.org/git/gcc.git
cd gcc

git remote add github git@github.com:andmeics/gcc.git

REMOTE=github
BRANCH=$(git rev-parse --abbrev-ref HEAD)
BATCH_SIZE=10000

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
git push -u github --all
git push -u github --tags

# git push --mirror github
cd ..
git clone --bare git://gcc.gnu.org/git/gcc.git
cd gcc.git
git remote add github git@github.com:andmeics/gcc.git
git push --mirror github
