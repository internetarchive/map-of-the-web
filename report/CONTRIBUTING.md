# Map of the Web Contribution Guidelines

This document contains information of use to developers looking to
improve the Map of the Web's codebase.  See [README.md](README.md) for an
introduction to this project. All discussions about the Map of the Web fall under our [code of conduct](docs/CODE_OF_CONDUCT.md).

## Submitting and Reviewing Code

This repository has a home on
[GitHub](https://github.com/internetarchive/map-of-the-web).  Please submit
[pull requests](https://help.github.com/articles/about-pull-requests/)
(PRs) there.

Please submit changes via pull request, even if you have direct commit
access to the repository.  The PR process allows us to get additional
eyes on change proposals.

As you work on your branch, try to test it locally to ensure that it
still builds and deploys properly, and that you haven't introduced new
accessibility bugs.

Generally, the more controversial, complex or large a change, the more
opportunity people should have to comment on it.  That means it should
garner more comments/approvals, or it means it should sit longer
before being merged. You can talk with us about a change you'd like to
make before or while you work on it. We
don't have hard rules about such things, and documentation changes
usually don't need to sit as long as functional changes, but figure a
business day or two for an average patch to get discussed.

As to when to merge, that's a judgment call.  Usually once an "approved"
review goes through, and there aren't any more changes requested, then
the author of the PR will merge it (if they have access to push to
master).  Generally, wait to merge until the conversation around a
change has concluded.  If you're unsure, ask!  "Is this ready to merge?"
is often a useful next step in the conversation.

If your PR fixes a bug or adds a feature, please write a test to go with
the change.  If the change involves libraries or would be difficult to
test, please use a Given-When-Then description like or describe in your PR message how reviewers should test that your change works as expected.

### Document as you go

If you introduce a new framework or dependency, add the necessary
information to [INSTALL.md](INSTALL.md) and the other documentation.

### The "Obvious Fix" rule: committing some minor changes directly to 'master'

Certain kinds of presumed-safe changes may be reviewed post-commit
instead of pre-commit, meaning that they can be committed directly to
`master` without going through a PR, when the committer has push
access to do so.

The purpose of this is to save time for busy developers.  It avoids
the low-but-still-noticeable overhead of the PR review process for
changes where the that process would not provide much additional
protection beyond what post-commit review provides anyway.  In
practice, that means the following kinds of changes:

* Clear typo fixes.

  If there's an obvious typo that doesn't affect code flow (e.g., a
  typo in a code comment, or even in a user-visible string), you can
  just fix it.  However, if the typo affects code behavior, other than
  in how user-visible text is displayed, then it should go through the
  normal PR review process.

* Whitespace and formatting cleanups.

  Commits that are formatting-only and make the code more compliant
  with our coding guidelines can just be committed directly.  There is
  no need to take a reviewer's time with them.

* Developer documentation changes.

  If the substance of a development documentation change is agreed on,
  and it's just a matter of wording, then the change can just be
  committed directly, since after all, it's easy to improve it later.
  (For example, the commit that added this section to this document
  would qualify.)

  Substantive changes to user-facing documentation should, of course,
  still go through the normal PR process.

Developers should always exercise judgment, of course.  It's always
okay to still use a PR for a change qualifies as an "obvious fix", and
if one thinks there is any chance of controversy or disagreement about
the change, then the best thing to do is put it into a PR so it can go
through the regular review process.

### Branching and Branch Names

We do all development on lightweight branches, with each branch
encapsulating one logical changeset (that is, one group of related
commits).  Please try to keep changesets small and well-bounded: a
branch should usually be short-lived, and should be turned into a PR,
reviewed, and merged to `master` as soon as possible.  Keeping
branches short-lived reduces the likelihood of conflicts when it comes
time to merge them back into master.

When a branch is associated with an issue ticket, then the branch name
should start with the issue number and then give a very brief summary,
with hyphens as the separator, e.g.:

    871-fix-provider-risk-score

Everything after the issue number is just a reminder what the branch
addresses.  Sometimes a branch may address only part of an issue, and
that's fine: different branches can start with the same issue number,
as long as the summary following the issue number indicates what part
of the issue that particular branch addresses.

If there is no issue number associated with a branch, then don't start
the branch name with a number.

While there are no strict rules on how to summarize a branch's purpose
in its name, it may help to keep in mind some common starting words:
"`fix`", "`feature`", "`refactor`", "`remove`", "`improve`", and "`test`".

### Rebases and force-pushes

Force pushes (after a rebase or a `commit --amend`) are currently
allowed everywhere except the master branch.  This repository has master
as a "protected" branch, meaning force-pushes are disabled
automatically.  If you're working with someone else on a shared branch
you should talk with them before changing shared history.  We expect
force-pushing to mostly occur in active PR branches.

### Commit Messages

#### Follow Best Practices

Please adhere
to [these guidelines](https://chris.beams.io/posts/git-commit/) for
each commit message.  The "Seven Rules" described in that post are:

1. Separate subject from body with a blank line
2. Limit the subject line to 50 characters
3. Capitalize the subject line
4. Do not end the subject line with a period
5. Use the imperative mood in the subject line
6. Wrap the body at 72 characters
7. Use the body to explain _what_ and _why_ vs. _how_

Think of the commit message as an introduction to the change.  A
reviewer will read the commit message right before reading the diff
itself, so the commit message's purpose is to put the reader in the
right frame of mind to understand the code change.

The reason for the short initial summary line is to support commands,
such as `git show-branch`, that list changes by showing just the first
line of each one's commit message.

#### Reference Issues

If the commit is related to one or more issues, please include both the issue
number (as shown in the GitHub UI and URL) and the title of each issue near the
end of the commit message (but before co-authors). We've been formatting these
like so:

```
Issue #12 This is the title of a very long issue which needs to be
          wrapped to avoid going over 72 characters
Issue #34 Another, shorter, issue title
```

Including the issue number (with the `#` prefix) allows the GitHub UI to
[automatically link the commit to the
issue](https://help.github.com/articles/autolinked-references-and-urls/#issues-and-pull-requests),
and including the issue title makes it easier to understand the context of a
change without needing to go to the issue tracker.

#### Credit Co-authors

If you paired with someone on your change, or if you are incorporating the work
of someone else in your commit, please give them due credit with
`Co-authored-by` line(s) at the end of the commit message. See GitHub's user
documentation on [Creating a commit with multiple
authors](https://help.github.com/articles/creating-a-commit-with-multiple-authors/)
for more details.

### Indentation and Whitespace

Please uses spaces, never tabs.  Indent Python code by 4 spaces per
level, XML by 2 spaces per level, and avoid trailing whitespaces.  The
file [.editorconfig](.editorconfig), in the repository's root
directory, encodes these formatting conventions in a way that most
text editors can read.

Sometimes commits make it through without following these guidelines.
When you find yourself about to make changes to such code,
please first make a whitespace-only commit to regularize the
indentation, and then make a separate commit with your code changes.

### Licensing Your Contribution
The Map of the Web is published under the terms of version 3 of the
[GNU Affero](https://www.gnu.org/licenses/agpl-3.0.en.html/).  It is
important that the codebase continue to be publishable under that
license.  To make that possible, here are some guidelines on including
3rd party code in the codebase.

If you submit code that you wrote or that you have authority to submit
from your employer or institution, you give it to us under version 3
of the GNU Affero License.

Please make the license of the code clear in your pull request.  Tell
us who wrote it, if that isn't just you.  If the code was written for
an employer, tell us that too.  Tell us what license applies to the
code, especially if it differs from the project's GNU Affero 3.0 license.

If you submit code that doesn't come from you or your employer, we
call that "Third-Party Code" and have a few requirements.  If the code
contains a license statement, that's great.  If not, please tell us
the license that applies to the code and provide links to whatever
resources you used to find that out. For some examples, see the
LICENSE and METADATA parts of [Google's guide to introducing
third-party code](https://opensource.google.com/docs/thirdparty/documentation/#license).

If your submission doesn't include Third Party Code, but instead
depends on it in some other way, we might need a copy of that
software.  Your submission should tell us where and how to get it as
well as the license that applies to that code.  We will archive a copy
of that code if we accept your pull request.

### Expunge Branches Once They Are Merged

Once a branch has been merged to `master`, please delete the branch.
You can do this via the GitHub PR management interface (it offers a
button to delete the branch, once the PR has been merged), or if
necessary you can do it from the command line:

    # Make sure you're not on the branch you want to delete.
    $ git branch | grep '^\* '
    * master

    # No output from this == up-to-date, nothing to fetch.
    $ git fetch --dry-run

    # Delete the branch locally, if necessary.
    $ git branch -d some-now-fully-merged-branch

    # Delete it upstream.
    $ git push origin --delete some-now-fully-merged-branch

## Avoiding Generatable Elements In The Repo

As a general rule, we try to keep generated elements out of the
repository.  This includes files that result from build processes.  If
we want to memorialize a compiled version of the program, the best way
to do that is with tags or to record that information and put the
saved version somewhere other than this repository.  If a file can be
generated from the materials in the repository using
commonly-available tools, please do not put it in the repository
without raising it for discussion.

## Thank you!

The Map of the Web will help us understand the shape of the Internet Archive's
crawl efforts, and improve the reliability of the Internet! We're glad to have
your help getting there faster.
