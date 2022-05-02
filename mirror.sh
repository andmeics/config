#!/bin/bash
# The first stage submits the main branch first
git clone https://github.com/llvm/llvm-project.git
cd llvm-project

git remote rename origin old.origin
git remote add origin git@github.com:andmeics/llvm-project.git


REMOTE=origin
BRANCH=$(git rev-parse --abbrev-ref HEAD)
BATCH_SIZE=10000 #

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
git push -u origin --all
git push -u origin --tags
# git push --mirror origin


# The third stage fills in the remaining information and makes a complete mirror
# git clone --bare https://github.com/llvm/llvm-project.git
git clone --mirror https://github.com/llvm/llvm-project.git
cd llvm-project.git
git push --mirror git@github.com:andmeics/llvm-project.git

# The fourth stage is continuously updated, and the warehouse is regularly synchronized. The actions here are performed regularly.
cd llvm-project.git
git fetch --all
git push --mirror git@github.com:andmeics/llvm-project.git
